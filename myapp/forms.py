from django import forms
from myapp.models import OrderItem

class OrderItemForm(forms.Form):
    client_choices = (
        ('0', 'ZiadKobti'),
        ('1', 'UsamaMir'),
        ('2', 'SajaMansouri'),
        ('3', 'PrashantRanga'),
        ('4', 'MarkSmith'),
    )

    client  = forms.ChoiceField(widget= forms.RadioSelect, choices=client_choices)

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity', 'client', 'status']


    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['client'].label = 'Client Name'


class InterestForm(forms.Form):
    INTEREST_CHOICES = (
        ('0','Yes'),
        ('1','No'),

    )

    interested = forms.ChoiceField(
        label='Interested',
        widget=forms.RadioSelect,
        initial=1,
        required=False,
        choices=INTEREST_CHOICES,
    )

    quantity = forms.IntegerField(
        label='Quantity',
        initial=1,
        min_value=1,
        required=False,
    )

    comments = forms.CharField(
        label='Additional Comments',
        widget=forms.Textarea,
        required=False,
    )