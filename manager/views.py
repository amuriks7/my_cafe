from django.shortcuts import render, redirect

from main_page.forms import UserReservationForm
from main_page.models import UserReservation


def reservation_list(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')
    else:
        reservation = UserReservationForm()

    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservation_list.html', context={'lst': lst, 'reservation': reservation})
