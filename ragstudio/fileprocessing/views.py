from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
import uuid
from markitdown import MarkItDown
from io import BytesIO

def fileupload(request):

    if request.method == 'POST':
        # file is uploaded. Convert to markdown and store in session and redirect to next step
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # convert the document to markdown format
            md = MarkItDown(enable_plugins=False)
            uploaded_file = form.cleaned_data['file']
            binary_text = BytesIO(uploaded_file.read())
            markdown_text = md.convert_stream(binary_text)

            # generate unique id and store in session
            unique_id = str(uuid.uuid4())
            request.session[unique_id] = markdown_text

            chunking_context = {
                'step': 2,
                'text': markdown_text
            }

            return render(request=request, template_name='chunking.html', context=chunking_context)

    # render file upload form
    form = FileForm()
    file_upload_context = {
        'form': form,
        'step': 1
    }

    return render(request=request, template_name='fileupload.html', context=file_upload_context)

def chunking(request):

    if request.method == 'POST':
        # re-adjust chunking text as per the form
        pass

