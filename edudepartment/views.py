from django.shortcuts import render

def index(request):
	return render(request,'edudepartment/index.html')

def about(request):
	return render(request,'edudepartment/about.html')

def services(request):
	return render(request,'edudepartment/services.html')

def gallery(request):
	return render(request,'edudepartment/gallery.html')

def contact(request):
	return render(request,'edudepartment/contact.html')

def feedback(request):
	return render(request,'edudepartment/feedback.html')

def vision(request):
	return render(request,'edudepartment/vision.html')

def mision(request):
	return render(request,'edudepartment/mision.html')
