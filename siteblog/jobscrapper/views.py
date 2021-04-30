from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def vacancies_view(request):

    form = FindForm()

    city = request.GET.get("city")
    occupation = request.GET.get("occupation")
    qs = []
    if city or occupation:
        _filter = {}
        if city:
            _filter["city__slug"] = city
        if occupation:
            _filter["occupation__slug"] = occupation


        qs = Vacancy.objects.filter(**_filter)
    else:
        qs = Vacancy.objects.all()

    context = {
        "vacancies": qs,
        "form": form,
    }
    return render(request, "jobscrapper/vacancies.html", context)

