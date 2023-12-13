from django.shortcuts import redirect, render
from django.shortcuts import render
from django.views.generic import View
from work.forms import EmpForm,BookForm
from work.models import Book


# Create your views here.
class Emp(View):
 def get(self,request):
    form=EmpForm()
    return render(request,"add.html",{"form":form})


class Bookviw(View):
  def get(self,request):
    form=BookForm()
    return render(request,"book.html",{"form":form})
  
  def post(self,request):
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()



      print("crated")
      return render(request,"book.html",{"form":form})
    else:
      return render(request,"book.html",{"form":form})
    
class Booklist(View):
  def get(self,request):
    qs = Book.objects.all()
    return render(request,"booklist.html",{"qs":qs})
    

class Book_detailview(View):

  def get(self,request,*args,**kwargs):

    print(kwargs)
    id=kwargs.get("pk")

    qs =Book.objects.get(id=id)
    return render(request,"books.html",{"data":qs})
  
class Book_delete(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("pk")
    Book.objects.get(id=id).delete()
    return redirect("book-all")
    

  

