from django.shortcuts import render

# Create your views here.


async def index(request):
    context = {"username": "pessimist"}
    return render(request, "community/index.html", context)


def page_404(request, exception):
    return render(request, "404.html", {}, status=404)
