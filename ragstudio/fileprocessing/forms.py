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
    CHUNKING_STRATEGY_CHOICES = [
        ('fixed', 'Fixed'),
        ('recursive','Recursive'),
        ('semantic', 'Semantic')
    ]
    chunking_strategy = forms.ChoiceField(choices=CHUNKING_STRATEGY_CHOICES, widget=forms.Select(attrs={'class':'form-select'}))

    # fixed size chunking field
    chunk_size = forms.IntegerField(label='Chunk Size', required=False, widget=forms.NumberInput(attrs={'class':'conditional-chunking-arg fixed-chunk form-control'}))
    chunk_overlap = forms.IntegerField(label='Chunk Overlap', required=False, widget=forms.NumberInput(attrs={'class':'conditional-chunking-arg fixed-chunk form-control'}))



class EmbeddingForm(forms.Form):
    age = forms.IntegerField(label="Age")

class LlmQuery(forms.Form):
    feedback = forms.CharField(label="feedback")