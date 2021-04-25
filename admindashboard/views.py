from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from contacts.models import *
from listings.models import *
from realtors.models import *
from .forms import *
import os


# Create your views here.

def index(request):
    contact_count = Contacts.objects.all().count()
    realtor_count = Realtor.objects.all().count()
    listing_count = Listing.objects.all().count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'contact': contact_count,
        'realtor': realtor_count,
        'listing': listing_count,
        'user': user_count,
        'admin': admin_count,
    }
    return render(request,'admindashboard/admin.html', context)

# listing

def listing(request):
    listing = Listing.objects.all()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Listing Added Successfully')
            return redirect('/admins/listing')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Listing')
            return render(request, 'admins/listing.html', {'form': form})
    context = {
        'listing': listing,
        'form': ListingForm
    }
    return render(request, 'admindashboard/listing.html', context)

def delete_listing(request, l_id):
    listing = Listing.objects.get(id=l_id)
    os.remove(listing.photo_main.path)
    listing.delete()
    return redirect("/admins/listing")


def update_listing(request, l_id):
    listing = Listing.objects.all()
    instance = Listing.objects.get(id=l_id)
    prev_image = instance.photo_main.path
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            new_image = instance.photo_main.path
            if prev_image != new_image:
                os.remove(prev_image)
            messages.add_message(request, messages.SUCCESS, 'listing updated Successfully')
            return redirect('/admins/listing')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update listing')
            return render(request, "admindashboard/listing.html", {'form': ListingForm(instance=instance), "listing": listing})
    context = {'form': ListingForm(instance=instance), "listing": listing}
    return render(request, "admindashboard/listing.html", context)

# users

def getUsers(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'admindashboard/user.html', context)

# def delete_user(request, username):
#     user = User.objects.get(username=username)
#     user.delete()
#     return redirect('adminUsers')


def update_user_to_admin(request, user_id):
    user = User.objects.get(username=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User has been updated to Admin')
    return redirect('/admins/users')

    # contact

def contact(request):
    contact = Contacts.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Contact Added Successfully')
            return redirect('/admins/contact')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Contact')
            return render(request, 'admins/contact.html', {'form': form})
    context = {
        'contact':contact,
        'form': ContactForm

    }
    return render(request, 'admindashboard/contact.html', context)

def delete_contact(request, c_id):
    contact = Contacts.objects.get(id=c_id)
    contact.delete()
    return redirect("/admins/contact")

def update_contact(request, c_id):
    contact = Contacts.objects.all()
    instance = Contacts.objects.get(id=c_id)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'contact updated Successfully')
            return redirect('/admins/realtor')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update contact')
            return render(request, "admindashboard/contact.html", {'form': ContactForm(instance=instance), "contact": contact})
    context = {'form': ContactForm(instance=instance), "contact": contact}
    return render(request, "admindashboard/contact.html", context)

    #realtor

def realtor(request):
    realtor = Realtor.objects.all()
    if request.method == 'POST':
        form = RealtorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Realtor Added Successfully')
            return redirect('/admins/realtor')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Realtor')
            return render(request, 'admins/realtor.html', {'form': form})
    context = {
        'realtor':realtor,
        'form':RealtorForm
    }
    return render(request, 'admindashboard/realtor.html', context)

def delete_realtor(request, r_id):
    realtor = Realtor.objects.get(id=r_id)
    realtor.delete()
    return redirect("/admins/realtor")

def update_realtor(request, r_id):
    realtor = Realtor.objects.all()
    instance = Realtor.objects.get(id=r_id)
    prev_image = instance.photo.path
    if request.method == "POST":
        form = RealtorForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            new_image = instance.photo.path
            if prev_image != new_image:
                os.remove(prev_image)
            messages.add_message(request, messages.SUCCESS, 'realtor updated Successfully')
            return redirect('/admins/realtor')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update realtor')
            return render(request, "admindashboard/realtor.html", {'form': RealtorForm(instance=instance), "listing": listing})
    context = {'form': RealtorForm(instance=instance), "realtor": realtor}
    return render(request, "admindashboard/realtor.html", context)