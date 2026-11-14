from django.conf import settings
from django.utils.translation import activate

def set_language_from_browser(request):
    if not request.session.get('django_language'):
        # Get browser's preferred language
        browser_lang = request.LANGUAGE_CODE
        if browser_lang in dict(settings.LANGUAGES):
            request.session['django_language'] = browser_lang
            activate(browser_lang)
