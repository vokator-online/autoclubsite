from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html', {})

def events(request):
    return render(request, 'main/events.html', {})

def cinema(request):
    return render(request, 'main/cinema.html', {})

def meetings(request):
    return render(request, 'main/meetings.html', {})

def applications(request):
    return render(request, 'main/applications.html', {})

def merchandise(request):
    return render(request, 'main/merchandise.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('name')
        message_email = request.POST.get('email')
        message_subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Patikrinkite, ar visi laukai buvo pateikti
        if not all([message_name, message_email, message_subject, message]):
            # Galite pridėti pranešimą naudotojui apie trūkstamus laukus
            messages.error(request, "Please fill out all fields.")
            return redirect('contact')  # 'contact' yra URL pavadinimas tam pačiam puslapiui

        send_mail(
            message_subject,
            message,
            message_email,
            ['puthon.pychton@gmail.com'],
            fail_silently=False,
        )

        # Galite pridėti sėkmingo veiksmo pranešimą naudotojui
        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')  # Peradresavimas į tą patį puslapį rodo sėkmės pranešimą

    else:
        return render(request, 'main/contact.html', {})
    