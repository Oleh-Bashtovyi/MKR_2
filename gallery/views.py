from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Category, Image


def gallery_view(request):
    categories = Category.objects.all()
    return render(request, 'gallery.html', {'categories': categories})


def image_detail(request, pk):
    image = get_object_or_404(Image, id=pk)
    return render(request, 'image_detail.html', {'image': image})
