from django import forms

class OneOnOneForm(forms.Form):
    team = forms.ChoiceField(
        choices=[
            (1, 'England'),
            (2, 'Australia'),
            (3, 'South Africa'),
            (4, 'West Indies'),
            (5, 'New Zealand'),
            (6, 'India'),
            (7, 'Pakistan'),
            (8, 'Sri Lanka'),
            (9, 'Zimbabwe'),
            (11, 'United States of America'),
            (12, 'Bermuda'),
            (14, 'East Africa'),
            (15, 'Netherlands'),
            (17, 'Canada'),
            (19, 'Hong Kong'),
            (20, 'Papua New Guinea'),
            (25, 'Bangladesh'),
            (26, 'Kenya'),
            (27, 'United Arab Emirates'),
            (28, 'Namibia'),
            (29, 'Ireland'),
            (30, 'Scotland'),
            (32, 'Nepal')
        ],
        label="Select Your Team"
    )
    
    opponent = forms.ChoiceField(
        choices=[
            (1, 'England'),
            (2, 'Australia'),
            (3, 'South Africa'),
            (4, 'West Indies'),
            (5, 'New Zealand'),
            (6, 'India'),
            (7, 'Pakistan'),
            (8, 'Sri Lanka'),
            (9, 'Zimbabwe'),
            (11, 'United States of America'),
            (12, 'Bermuda'),
            (14, 'East Africa'),
            (15, 'Netherlands'),
            (17, 'Canada'),
            (19, 'Hong Kong'),
            (20, 'Papua New Guinea'),
            (25, 'Bangladesh'),
            (26, 'Kenya'),
            (27, 'United Arab Emirates'),
            (28, 'Namibia'),
            (29, 'Ireland'),
            (30, 'Scotland'),
            (32, 'Nepal')
        ],
        label="Select Opponent Team"
    )
