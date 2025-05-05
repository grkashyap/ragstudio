from django import forms

class FileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput())

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']

        # 1 MB limit
        max_size = 1 * 1024 * 1024
        if uploaded_file.size > max_size:
            raise forms.validationError("File size must be under 1 MB")

        # supports text and pdf only
        valid_mime_types = ['text/plain','application/pdf']
        if uploaded_file.content_type not in valid_mime_types:
            raise forms.validationError("Unsupported file type. Allowed file types are .txt and .pdf")

        return uploaded_file

class ChunkingForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='Preview (First 10 lines)')

class EmbeddingForm(forms.Form):
    age = forms.IntegerField(label="Age")

class LlmQuery(forms.Form):
    feedback = forms.CharField(label="feedback")