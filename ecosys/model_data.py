# -*- coding: utf-8

LANGUAGES = (
    ('BG', 'Bulgarian'),
    ('CS', 'Czech'),
    ('DA', 'Danish'),
    ('DE', 'German'),
    ('EL', 'Greek'),
    ('EN', 'English'),
    ('ES', 'Spanish'),
    ('ET', 'Estonian'),
    ('FI', 'Finnish'),
    ('FR', 'French'),
    ('GA', 'Irish'),
    ('H', 'Hungarian'),
    ('IS', 'Icelandic'),
    ('IT', 'Italian'),
    ('LB', 'Luxembourgish'),
    ('LT', 'Lithuanian'),
    ('LV', 'Latvian'),
    ('MT', 'Maltese'),
    ('NL', 'Dutch'),
    ('NO', 'Norwegian'),
    ('PL', 'Polish'),
    ('PT', 'Portuguese'),
    ('RM', 'Rhaeto-Romance'),
    ('RO', 'Romanian'),
    ('SK', 'Slovak'),
    ('SL', 'Slovenian'),
    ('SV', 'Swedish'),
    ('TR', 'Turkish'),
)

RESOURCE_TYPES = (
    ('Literature', 'Literature'),
    ('Tool', 'Tool'),
    ('Event', 'Event'),
    ('Website', 'Website'),
    ('Maps', 'Maps'),
)

ORIGIN_DATA = ('Science/academic organisation',
               'Policy/governmental organisation',
               'Science-policy interface',
               'Field practitioner/Manager',)
ORIGIN = [(i, i) for i in ORIGIN_DATA]

STATUS = (
    ('Draft', 'Draft'),
    ('Final', 'Final'),
    ('I don\'t know', 'I don\'t know'),
)

AVAILABILITY = (
    ('Free of charge', 'Free of charge'),
    ('With costs', 'With costs'),
    ('I don\'t know', 'I don\'t know'),
)

YES_NO = (
    ('0', 'No'),
    ('1', 'Yes'),
)

SPATIAL_SCALE = (
    ('International', 'International'),
    ('National', 'National'),
    ('Regional', 'Regional'),
    ('Local', 'Local'),
    ('Required', 'Required'),
)

COUNTRIES = (
    ('AL', 'Albania'),
    ('AT', 'Austria'),
    ('BA', 'Bosnia-Herzegovina'),
    ('BE', 'Belgium'),
    ('BG', 'Bulgaria'),
    ('CH', 'Switzerland'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DE', 'Germany'),
    ('DK', 'Denmark'),
    ('EE', 'Estonia'),
    ('ES', 'Spain'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GB', 'United Kingdom'),
    ('GR', 'Greece'),
    ('HR', 'Croatia'),
    ('H', 'Hungary'),
    ('IE', 'Ireland'),
    ('IS', 'Iceland'),
    ('IT', 'Italy'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('L', 'Luxembourg'),
    ('LV', 'Latvia'),
    ('ME', 'Montenegro'),
    ('MK', 'Macedonia (FYR)'),
    ('MT', 'Malta'),
    ('NL', 'Netherlands'),
    ('NO', 'Norway'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('RO', 'Romania'),
    ('RS', 'Serbia'),
    ('SE', 'Sweden'),
    ('SI', 'Slovenia'),
    ('SK', 'Slovakia'),
    ('TR', 'Turkey'),
)

CONTENT_DATA = (
    'Theoretical material for ecosystem assessment (methods, concepts, guidance)',
    'Analytical material (Ecosystem assessment case-studies)',
    'Communication material on ecosystem assessment (maps)',
    'Policy document (Strategies, Directives)',
    'Produce/Evaluate data (measured, observed, modelled)',
    'Produce maps',
    'Mandatory reporting to EU or international body',)
CONTENT = [(i, i) for i in CONTENT_DATA]

KEY_ELEMENTS_DATA = (
    'Setting the assessment process (incl. governance, stakeholder engagement, funding, communication, ...)',
    'Conceptual framework',
    'Biophysical baseline of ecosystems and their services (mapping and assessment of state & trends)',
    'Valuation of ecosystem services (links between ecosystem services and human well-being)',
    'Scenario development and analyses',
    'Policy analyses or response options',)
KEY_ELEMENTS = [(i, i) for i in KEY_ELEMENTS_DATA]
