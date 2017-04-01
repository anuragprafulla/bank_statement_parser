from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import Statement, Transaction, User 
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core import serializers

# Create your views here.
def index(request):
    return HttpResponse("Hello. We will help you manage your bank statements.")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Statements(statement=request.FILES['file.'])
            instance.save()
            return HttpResponseRedirect('/upload/success')
    else:
        form = UploadFileForm()
       
    return render(request, 'upload.html',{'form':form})


def upload(request):
    if request.method == 'POST': # and request.FILES['myfile']:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['file']
            s = Statement(statement=myfile)
            s.save()
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'upload_complete.html',{
                'uploaded_file_url': uploaded_file_url
            })
    else:
        form = UploadFileForm()
 
    return render(request, 'upload.html', {'form':form})

def list(request):
    username = request.GET['name'];
    user = User.objects.get(name=username)
    user_id = user.id;
    queryset = Transaction.objects.filter(user=user_id)
    queryset = serializers.serialize('json', queryset)
#    return HttpResponse(queryset)
    return HttpResponse(queryset, content_type="application/json")

def search(request):
#    if request.method= 'GET':
#        name = request.GET['name']
#        user = User.objects.filter(name=name).count()

         
    return render(request, 'search.html')
