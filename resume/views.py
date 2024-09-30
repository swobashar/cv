from django.shortcuts import render
from .models import Biodata,Profession_Video

# Create your views here.

def home(request):
	all_pdf_resume = Biodata.objects.all()
	all_professional_videos = Profession_Video.objects.all()
	return render(request,'index-1.html',{'all_pdf_resume':all_pdf_resume,'all_professional_videos':all_professional_videos})
