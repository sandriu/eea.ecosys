import time
import requests


frame = None
last_hit = None
TIMEOUT = 3600 #seconds
FRAME_URL = 'http://biodiversity.europa.eu/ecosystem-assessments/frame'
MARKER = '<!--SITE_HEADERFOOTER_MARKER-->'


def get_frame_contents():
    """ Simply http-request the html produced by Zope """
    tries = 3
    while tries:
        resp = requests.get(FRAME_URL)
        if resp.status_code == 200:
            return resp.text
        tries -= 1
    return None


def prepare_frame(frame_contents):
    """ Make it extendable by layout template in our app """
    assert MARKER in frame_contents
    baseurl = FRAME_URL.rsplit('/', 1)[0]
    return frame_contents.replace(MARKER, '{% block frame_content %}{% endblock %}')\
        .replace('<title>Ecosystem Assessments in Europe - </title>',
                 '<title>Ecosystem Assessments in Europe - {% block title %}{% endblock %}</title>')\
        .replace('</head>', '{% block head %}{% endblock %}</head>')\
        .replace('<img src="images', '<img src="%s/images' % baseurl)


def load_template(name):
    global frame, last_hit
    if name is not 'frame':
        return None
    if frame is None or time.time() - last_hit > TIMEOUT:
        html = get_frame_contents()
        frame = prepare_frame(html)
        last_hit = time.time()

    return frame
