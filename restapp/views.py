from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.response import Response
import urllib.request, json

# WORKING
class Simple(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'simplehome.html'    

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/buttons.json") as url:
            data = json.loads(url.read().decode())
        return Response(data)

# WORKING
class Certificate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'certifications.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/certificates.json") as url:
            data = json.loads(url.read().decode())
        return Response({'all_certificates': data})

# WORKING
class Projects(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'projects.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/projects.json") as url:
            data = json.loads(url.read().decode())
        return Response({"allprojects": data})

# 
class WorkedFor(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'workedfor.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/workedfor.json") as url:
            data = json.loads(url.read().decode())
        return Response(data)

# Working
class Blogs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blogs.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/blogs.json") as url:
            data = json.loads(url.read().decode())
        return Response({"allblogs": data})


class OpenSource(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'opensource.html'

    def get(self, request):
        with urllib.request.urlopen("https://gauravghati.github.io/apis/opensource.json") as url:
            data = json.loads(url.read().decode())
        return Response(data)


class RidingSolo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ridingsolo.html'

    def get(self, request):
        return Response()

class GistPages(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'goodsentences.html'

    def get(self, request, pagename):
        print(pagename)
        with urllib.request.urlopen("https://gauravghati.github.io/apis/gistpages.json") as url:
            data = json.loads(url.read().decode())
        
        page = data[0]
        for x in data:
            if (x['pagename']==pagename):
                page=x
        
        return Response(page)

# Review Email Config (NOT WORKING FOR NOW)

# from restapp.models import Reviews
# import smtplib
# class Home(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'

#     def get(self, request):
#         with urllib.request.urlopen("https://gauravghati.github.io/apis/home.json") as url:
#             data = json.loads(url.read().decode())
#         return Response(data)

#     def post(self, request):
#         name = request.POST.get('name')
#         toemail = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         text = 'Thanks For sharing your opinion on my Website, I will get back you ASAP! ;)'
#         review = Reviews(name=name, email=toemail, subject=subject, message=message)
#         review.save()

#         my_mail = "gauravghati225@gmail.com"

#         # Prepare actual message
#         message1 = """From: %s\nTo: %s\nSubject: %s\n\n%s
#         """ % (my_mail, toemail, subject, text)

#         message2 = """From: %s\nTo: %s\nSubject: %s\n\n%s
#         """ % (my_mail, my_mail, subject, message)

#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.connect("smtp.gmail.com", 587)
#         server.ehlo()
#         server.starttls()
#         server.ehlo()
#         server.login(my_mail, "xfuzvqgjizzdzopn")
#         server.sendmail(my_mail, toemail, message1)
#         server.sendmail(my_mail, my_mail, message2)
#         server.quit()
#         return redirect('home')
