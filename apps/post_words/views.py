from django.shortcuts import render, redirect, HttpResponse

def index(request):
    request.session['posts'] = []
    return render(request, "post_words/index.html")

def process(request):
    if request.method == "POST":
        if len(request.POST['word']) == 0:
            request.session["word"] = "You didn't post a word!"
        else:
            request.session["word"] = request.POST["word"]
        if "color" not in request.POST:
            request.session["color"] = "black"
        else:
            request.session["color"] = request.POST["color"]
        if "font_size" not in request.POST:
            request.session['font_size'] = "medium"
        else:
            request.session['font_size'] = request.POST["font_size"]

        request.session['posted_word'] = {
            "word": request.session["word"],
            "color": request.session["color"],
            "font_size": request.session['font_size']
        }

        request.session['posts'].append(request.session['posted_word'])

        print('*' * 50)
        print('*' * 50)
        print(request.session['posts'])
        print('*' * 50)
        print('*' * 50)

        if len(request.session['posts']) > 5:
            request.session['posts'].pop(0)


    return redirect("/display")

def display(request):
    return render(request, "post_words/index.html")

def clear(request):
    return redirect('/')
