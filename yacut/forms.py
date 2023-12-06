from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import SHORT_LEN, REGULAR


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Ссылка не валидна')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=SHORT_LEN),
            Optional(),
            Regexp(REGULAR,
                   message='Используйте буквы латинского алфавита и цифры')]
    )
    submit = SubmitField('Создать')
