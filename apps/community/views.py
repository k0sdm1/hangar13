from django.shortcuts import render

# Create your views here.


async def index(request):
    context = {"username": request.user.username if request.user.is_authenticated else "stranger"}
    return render(request, "community/index.html", context)


def page_404(request, exception):
    return render(request, "404.html", {}, status=404)
