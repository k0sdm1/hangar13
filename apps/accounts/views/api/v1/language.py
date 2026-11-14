from django.conf import settings
from django.utils.translation import activate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SetLanguageView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        language = request.data.get('language')
        
        # Validate language
        if language not in dict(settings.LANGUAGES):
            return Response(
                {'error': 'Invalid language code'}, 
                status=400
            )
        
        # Save to user profile or session
        request.user.preferred_language = language
        request.user.save()
        
        # Also set the session cookie for any future server-side requests
        request.session['django_language'] = language
        
        return Response({
            'status': 'success',
            'language': language
        })

    def get(self, request):
        # Return the user's current preferred language
        lang = getattr(request.user, 'preferred_language', None)
        if not lang:
            lang = request.session.get('django_language', settings.LANGUAGE_CODE)
        return Response({'language': lang})