from flask import (Blueprint, request, abort, render_template)
from ecosys import forms


library = Blueprint('library', __name__)


@library.route('/')
def home():
    return ''


@library.route('/add/<string:resource_type>', methods=['GET', 'POST'])
def edit(resource_type):
    try:
        ResourceForm, ReviewForm = forms.FORMS[resource_type]
    except KeyError:
        abort(404)

    resource_form = ResourceForm(resource_type=resource_type)
    review_form = ReviewForm()

    if request.method == 'POST':
        if resource_form.validate() and review_form.validate():
            resource = resource_form.save()
            review_form.save(resource)

    return render_template('edit.html', resource_form=resource_form,
                           review_form=review_form)