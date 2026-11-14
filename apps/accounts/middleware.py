from django.utils import translation
from django.conf import settings

class LanguagePreferenceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If user is authenticated, set their preferred language
        if request.user and request.user.is_authenticated:
            user_lang = getattr(request.user, 'preferred_language', None)
            if user_lang and user_lang in dict(settings.LANGUAGES):
                translation.activate(user_lang)
                request.LANGUAGE_CODE = user_lang
        
        response = self.get_response(request)
        return response