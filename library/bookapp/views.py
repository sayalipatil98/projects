from django.shortcuts import render,redirect
from .forms import bookform
from .models import book

# Create your views here.
def bookview(request):
    form=bookform()
    template_name="bookapp/bookfrom.html"
    context={"form":form}
    if request.method=="POST":
        form=bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request,template_name,context)

def showview(request):
    data=book.objects.all()
    template_name="bookapp/show.html"
    context={"data":data}
    return render(request,template_name,context)

def updateview(request,id):
    data=book.objects.get(bookid=id)
    form=bookform(instance=data)
    template_name="bookapp/bookform.html"
    context={'form':form}
    if request.method=="POST":
        form=bookform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request,template_name,context)

def delete(request,id):
    obj=book.objects.get(bookid=id)
    template_name="bookapp/conformation.html"
    context={'obj':obj}
    if request.method=="POST":
        obj.delete()
        return redirect('show_url')
    return render(request,template_name,context)


