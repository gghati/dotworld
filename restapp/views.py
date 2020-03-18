from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.response import Response
import urllib.request, json
from restapp.models import Reviews
import smtplib


class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restapp/index.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/home.json") as url:
            data = json.loads(url.read().decode())
        return Response(data)

    def post(self, request):
        name = request.POST.get('name')
        toemail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        text = 'Thanks For sharing your opinion on my Website, I will get back you ASAP! ;)'
        review = Reviews(name=name, email=toemail, subject=subject, message=message)
        review.save()

        my_mail = "gauravghati225@gmail.com"

        # Prepare actual message
        message1 = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (my_mail, toemail, subject, text)

        message2 = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (my_mail, my_mail, subject, message)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(my_mail, "xfuzvqgjizzdzopn")
        server.sendmail(my_mail, toemail, message1)
        server.sendmail(my_mail, my_mail, message2)
        server.quit()
        return redirect('home')


class Certificate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restapp/certifications.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/certificates.json") as url:
            data = json.loads(url.read().decode())
        return Response({'all_certificates': data})


class Projects(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restapp/projects.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/extra.json") as url:
            data = json.loads(url.read().decode())
        return Response(data)


class WorkExp(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'restapp/workexp.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/extra.json") as url:
            data = json.loads(url.read().decode())
        return Response(data)
