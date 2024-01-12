from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Blogs  # Import Contact from the same directory

def home(request):
    return render(request, "home.html")

def handleblog(request):
    posts = Blogs.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, "handleblog.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        fphoneno = request.POST.get("num")
        fdesc = request.POST.get("desc")
        query = Contact(name=fname, email=femail, phone_number=fphoneno, description=fdesc)
        query.save()
        messages.success(request, "Thanks for contacting us. We will get you back soon!")
        # messages.info(request, f"The name is {name}, the email is {email}, your phone no. is {phoneno}, and your query is {desc}.")
        return redirect("/contact")
    
    return render(request, "contact.html")
