from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if 'test' in title.lower():
    #         raise forms.ValidationError(
    #             'Test should not be included in a title')

    #     return title

    # def clean_content(self):
    #     content = self.cleaned_data.get('content')

    #     if 'test content' in content.lower():
    #         raise forms.ValidationError(
    #             'Test Content should not be included in a content')

    #     return content

    def clean(self):
        cleaned_data = self.cleaned_data

        title = cleaned_data.get('title')
        content = cleaned_data.get("content")

        # if there is already a clean_title method defined the title will be None here.
        print('Cleaned data', cleaned_data)

        if title.lower() == content.lower():
            # non-field validation for the whole form.
            raise forms.ValidationError(
                "Title and content must not be the same")

        if 'test content' in content.lower():
            # a field validation to content
            self.add_error(
                'content', 'Test Content should not be included in a content')

        return cleaned_data
