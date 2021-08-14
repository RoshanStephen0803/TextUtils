from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    dtext=request.POST.get('text','default')
    removedpunc=request.POST.get('removepunc','off')
    caps=request.POST.get('caps','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')

    if removedpunc=="on":
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in dtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Puctuations','analyzed_text':analyzed}
        dtext=analyzed

    if caps=="on":
        analyzed=""
        for char in dtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Uppercase','analyzed_text':analyzed}
        dtext=analyzed

    if newlineremove=="on":
        analyzed=""
        for char in dtext:
            if char !='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'New Line Removed','analyzed_text':analyzed}
        dtext=analyzed

    if spaceremove=="on":
        analyzed=""
        for index,char in enumerate(dtext):
            if not(dtext[index]==" " and dtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Extra space Remover','analyzed_text':analyzed}
        dtext=analyzed
   
    if (removedpunc!="on" and caps!="on" and newlineremove!="on" and spaceremove!="on"):
        return HttpResponse("Error")
        
    return render(request, 'analyze.html', params)
