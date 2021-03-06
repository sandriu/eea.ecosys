from datetime import datetime

from flask.ext.mongoengine.wtf import model_form
from flask.ext.uploads import UploadSet, AllExcept, SCRIPTS, EXECUTABLES
from flask.ext import wtf

from ecosys import models
from ecosys.forms.fields import *
from ecosys.model_data import *


files = UploadSet('files', AllExcept(SCRIPTS + EXECUTABLES))


_LiteratureForm = model_form(models.LiteratureReview)
_LiteratureResourceForm = model_form(models.Resource,
                                     exclude=['organizers', 'reviews'])


class EcosystemType(wtf.Form):

    COLSPAN = 10

    urban = MultiCheckboxField(pre_validate=False)

    cropland = MultiCheckboxField(pre_validate=False)

    grassland = MultiCheckboxField(pre_validate=False)

    woodland = MultiCheckboxField('Woodland & forest', pre_validate=False)

    heathland = MultiCheckboxField('Heathland & shrub', pre_validate=False)

    sparsely_vegetated_land = MultiCheckboxField('Sparsely vegetated land',
                                                 pre_validate=False)

    wetland = MultiCheckboxField(pre_validate=False)

    rivers_lakes = MultiCheckboxField('Rivers & lakes', pre_validate=False)

    marine = MultiCheckboxField(pre_validate=False)


class EcosystemServiceType(wtf.Form):

    COLSPAN = 4

    provisioning = MultiCheckboxField(pre_validate=False)

    regulating = MultiCheckboxField(pre_validate=False)

    cultural = MultiCheckboxField(pre_validate=False)


class LiteratureResourceForm(_LiteratureResourceForm):

    def __init__(self, *args, **kwargs):
        resource_type = kwargs.pop('resource_type')
        super(LiteratureResourceForm, self).__init__(*args, **kwargs)

        required_flag = wtf.Flags()
        required_flag.required = True

        self.resource_type.data = resource_type
        self.authors.validators = [wtf.validators.Required()]
        self.authors.flags = required_flag
        self.organisations.validators = [wtf.validators.Required()]
        self.organisations.flags = required_flag
        self.year_of_publication.validators = [wtf.validators.Required()]
        self.year_of_publication.flags = required_flag

    def save(self):
        resource = models.Resource()
        resource.title = self.data['title']
        resource.english_title = self.data['english_title']
        resource.language = self.data['language']
        resource.resource_type = self.data['resource_type']
        resource.authors = self.data['authors']
        resource.organisations = self.data['organisations']
        resource.year_of_publication = self.data['year_of_publication']
        resource.reviews = []
        return resource.save()


class LiteratureForm(_LiteratureForm):

    origin = wtf.SelectMultipleField('Origin of the document',
                                     choices=ORIGIN,
                                     validators=[wtf.validators.Required()])
    origin_other = wtf.TextField()

    filename = CustomFileField('File upload representing the document, if freely available',
       validators=[wtf.file_allowed(files, 'Document is not valid')])

    spatial = CustomBoolean('Spatial specificity', choices=YES_NO, default='0',
        validators=[RequiredIfChecked(fields=['spatial_scale', 'countries'],
                                      message='Spatial scale and Countries are required')])

    ecosystems = CustomBoolean('Are ecosystems studied?', choices=YES_NO,
        default='0')

    ecosystem_types_issues = wtf.FormField(EcosystemType,
        widget=EcosystemTableWidget(data=ECOSYSTEM_ISSUES, categ='Issues'))

    ecosystem_types_methods = wtf.FormField(EcosystemType,
        widget=EcosystemTableWidget(data=ECOSYSTEM_METHODS, categ='Methods',
                                    header=False))

    ecosystem_services = CustomBoolean('Are ecosystem services addressed?',
        choices=YES_NO, default='0')

    ecosystem_services_types = wtf.FormField(EcosystemServiceType,
        widget=EcosystemServiceTableWidget(data=ECOSYSTEM_TYPES))

    content = wtf.SelectMultipleField('Main content or purpose: mutliple select',
                                      choices=CONTENT,
                                      validators=[wtf.validators.Required()])
    content_other = wtf.TextField()

    feedback = wtf.SelectField('How did you came to know this document?',
                               choices=FEEDBACK,
                               validators=[wtf.validators.Required()])
    feedback_other = wtf.TextField()

    def __init__(self, *args, **kwargs):
        super(LiteratureForm, self).__init__(*args, **kwargs)

    def save(self, resource, user):
        review = models.LiteratureReview()

        origin = self.data['origin']
        origin_other = self.data['origin_other'].split(',')
        if origin_other:
            origin.extend(origin_other)

        review.origin = self.data['origin']
        review.status = self.data['status']
        review.availability = self.data['availability']
        review.languages = self.data['languages']
        review.url = self.data['url']

        filename = self.data['filename']
        file_saved = files.save(filename) if filename else ''
        review.filename = file_saved

        spatial = True if self.data['spatial'] == '1' else False
        review.spatial = spatial

        if int(review.spatial):
            review.spatial_scale = self.data['spatial_scale']
            review.countries = self.data['countries']

        review.spatial_scale = self.data['spatial_scale']
        review.countries = self.data['countries']
        review.content = self.data['content']
        review.key_elements = self.data['key_elements']

        feedback = self.data['feedback']
        feedback_other = self.data['feedback_other']
        if feedback_other:
            feedback = feedback_other
        review.feedback = feedback

        ecosystems = True if self.data['ecosystems'] == '1' else False
        review.ecosystems = ecosystems
        if ecosystems:
            review.ecosystem_types_issues = self.data['ecosystem_types_issues']
            review.ecosystem_types_methods = self.data['ecosystem_types_methods']

        ecosystem_services = True if self.data['ecosystem_services'] == '1' else False
        review.ecosystem_services = ecosystem_services
        if ecosystem_services:
            review.ecosystem_services_types = self.data['ecosystem_services_types']

        review.user = models.User.objects().get(id=user.id)
        review.datetime = datetime.now()
        resource.reviews.append(review)
        resource.save()


FORMS= {
    'literature': (LiteratureResourceForm, LiteratureForm),
}

