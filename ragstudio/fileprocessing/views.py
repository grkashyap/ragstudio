from django.shortcuts import render, redirect
from .forms import FileForm, ChunkingForm
import uuid
from markitdown import MarkItDown
from io import BytesIO
from .utils import chunk_document_fixed

def fileupload(request):
    """
        Method to handle file upload
    """
    if request.method == 'POST':
        # file is uploaded. Convert to markdown and store in session and redirect to next step
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # convert the document to Markdown format
            md = MarkItDown(enable_plugins=False)
            uploaded_file = form.cleaned_data['file']
            binary_text = BytesIO(uploaded_file.read())
            markdown_text = md.convert_stream(binary_text)

            # generate unique id and store in session
            unique_id = str(uuid.uuid4())
            data = {
                'markdown_text': str(markdown_text),
            }
            request.session[unique_id] = data

            return redirect('chunking', request_id=unique_id)

    # render file upload form
    form = FileForm()
    file_upload_context = {
        'form': form,
        'step': 1
    }

    return render(request=request, template_name='fileupload.html', context=file_upload_context)

def chunking(request, request_id):

    """
        Method to handle chunking
    """
    str_request_id = str(request_id)
    template = 'chunking.html'

    if request.method == 'POST':

        data = request.session.get(str_request_id)
        doc_text = data['markdown_text']
        trimmed_text = data['text']

        # re-adjust chunking text as per the form input
        chunking_form = ChunkingForm(request.POST)

        if chunking_form.is_valid():
            chunking_strategy = chunking_form.cleaned_data['chunking_strategy']

            if chunking_strategy == 'fixed':
                chunk_size = chunking_form.cleaned_data['chunk_size']
                chunk_overlap = chunking_form.cleaned_data['chunk_overlap']
                chunk_data = chunk_document_fixed(document_content=doc_text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)

                # set it to session and return context
                current_session_data = request.session.get(str_request_id)
                current_session_data['chunks'] = chunk_data
                request.session[str_request_id] = current_session_data

                chunking_context = {
                    'chunking_form': chunking_form,
                    'step': 2,
                    'text': trimmed_text,
                    'chunk_data': chunk_data
                }

                return render(request=request, template_name=template, context=chunking_context)

            elif chunking_strategy == 'recursive':
                pass
            elif chunking_strategy == 'semantic':
                pass

        return render(request=request, template_name=template, context={})
    else:

        data = request.session.get(str_request_id)
        chunking_form = ChunkingForm()

        file_content = data['markdown_text']
        text = "\n".join(file_content.splitlines()[:10])

        current_session_data = request.session.get(str_request_id)
        current_session_data['text'] = text
        request.session[str_request_id] = current_session_data

        chunking_context = {
            'chunking_form': chunking_form,
            'step': 2,
            'text': text,
            'chunk_data': ''
        }

        return render(request=request, template_name=template, context=chunking_context)
