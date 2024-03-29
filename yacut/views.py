from flask import flash, redirect, render_template, url_for

from . import app, db
from .models import URLMap
from .forms import URLMapForm
from .utils import is_short_id_unique, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if form.custom_id.data:
            if not is_short_id_unique(form.custom_id.data):
                flash('Предложенный вариант короткой ссылки уже существует.')
                return render_template('index.html', form=form)
            short_id = form.custom_id.data
        else:
            short_id = get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short_id
        )
        db.session.add(url_map)
        db.session.commit()
        flash('Ваша новая ссылка готова:')
        return render_template(
            'index.html',
            form=form,
            link=url_for('redirect_view', short_id=short_id, _external=True)
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original)
