from django import forms


class BadanieForm(forms.Form):
    kategorie = (
        (None, ''),
        ('Lekka', 'Lekka'),
        ('Ciężka', 'Ciężka'),
    )

    wapnowanie = (
        (None, ''),
        ('Potrzebne', 'Potrzebne'), #  (wysyłane, wyświetlane)
        ('Ograniczone', 'Ograniczone'),
        ('Zbędne', 'Zbędne'),
    )

    oznakowanie = forms.IntegerField(label="Oznakowanie", widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Oznakowanie próbki'}), required=True)
    kategoria = forms.ChoiceField(label="Kategoria", choices=kategorie, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}), required=False)
    pHwKCL = forms.FloatField(label='pHwKCL', widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Odczyn'}), required=False)
    potrz_wapn = forms.ChoiceField(label='Potrzeba wapnowania', choices=wapnowanie, widget=forms.Select(attrs={'class': 'form-control form-control-sm'}), required=False)
    p2o5 = forms.FloatField(label='P2O5', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość tlenku fosforu(V)'}), required=False)
    k2o = forms.FloatField(label='K2O', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość tlenku potasu'}), required=False)
    mg = forms.FloatField(label='Mg', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość magnezu'}), required=False)
    b = forms.FloatField(label='B', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość boru'}), required=False)
    mn = forms.FloatField(label='Mn', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość manganu'}), required=False)
    cu = forms.FloatField(label='Cu', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość miedzi'}), required=False)
    zn = forms.FloatField(label='Zn', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość cynku'}), required=False)
    fe = forms.FloatField(label='Fe', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Zawartość żelaza'}), required=False)
    lat = forms.FloatField(label='Lattitude', widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Szerokość geograficzne np.50.123454'}), required=False)
    long = forms.FloatField(label='Longitude', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Długość geograficzna 20.123454'}), required=False)