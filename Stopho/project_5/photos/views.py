from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import UploadImages
from django.views.generic import TemplateView

from .forms import HomeForm

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import state_union

def index(request):
     return render(request, 'base.html')

def image_list(request, image_slug=None):
    image = None
    photos = UploadImages.objects.all()
    if image_slug:
        image = get_object_or_404(UploadImages, slug=image_slug)
    return render(request, 'photos/Photo.html',{'image':image,'photos' : photos})

# def image_detail(request, id, slug):
#     images = get_object_or_404(UploadImages, id=id, slug=slug, available=True)
#     return render(request, 'photos/detail.html',{'images':images})


def search(request):
    if request.method == 'POST':
        search = request.POST["key_search"]
        search = search.lower().strip()
        print(search)
    stop_words = set(stopwords.words("english"))

    lemmatizer = WordNetLemmatizer()

    def tagwn(tag):
        if tag == 'NN' or tag == 'NNS' or tag == 'NNP' or tag == 'NNPS':
            return 'n'
        elif tag == 'VB' or tag == 'VBD' or tag == 'VBG' or tag == 'VBP' or tag == 'VBZ' or tag == 'VBN':
            return 'v'
        elif tag == 'RB' or tag == 'RBR' or tag == 'RBS':
            return 'r'
        else:
            return 'n'

    images = UploadImages.objects.all()
    image = []
    for desc in images:
        word_tokenize_list = word_tokenize(desc.description.lower())
        print(word_tokenize_list)
        word_pos_tag_list = nltk.pos_tag(word_tokenize_list)
        print(word_pos_tag_list)
        for word, tag in word_pos_tag_list:
            words_lemma = lemmatizer.lemmatize(word, tagwn(tag))
            print(words_lemma)
            if words_lemma == search:
                image.append(desc)

    return render(request, 'photos/search.html', {'search': search,'image': image})
