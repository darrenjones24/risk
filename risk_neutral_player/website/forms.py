from django import forms

INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 8)]


class PlayerForm(forms.Form):
    number_of_players = forms.IntegerField(
        label="Enter number of human players?",
        widget=forms.Select(choices=INTEGER_CHOICES),
    )


class LoseCountryForm(forms.Form):
    # overwrite __init__
    def __init__(self, request, *args, **kwargs):
        countries = kwargs.pop("countries", None)
        territories = [(country, country) for country in countries]
        super().__init__(*args, **kwargs)
        # extend __init__
        self.fields["loss"] = forms.CharField(widget=forms.Select(choices=territories))


class GainCountryForm(forms.Form):
    # overwrite __init__
    def __init__(self, request, *args, **kwargs):
        countries = kwargs.pop("countries", None)
        flat_list = [item for sublist in countries[:-1] for item in sublist]
        territories = [(country, country) for country in flat_list]
        territories.sort()
        super().__init__(*args, **kwargs)
        # extend __init__
        self.fields["gain"] = forms.CharField(widget=forms.Select(choices=territories))
