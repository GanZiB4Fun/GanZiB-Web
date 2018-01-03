from apps import app
from apps.book.views import book
from apps.category.views import category
from apps.index.views import index
from apps.search.views import search
from apps.sections.views import section
from apps.user.views import user

app.register_blueprint(index, url_prefix='/')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(category, url_prefix='/category')
app.register_blueprint(book, url_prefix='/book')
app.register_blueprint(search, url_prefix='/search')
app.register_blueprint(section, url_prefix='/section')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
