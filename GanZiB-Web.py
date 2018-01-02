from apps import app
from apps.category.views import category
from apps.index.views import index
from apps.user.views import user

app.register_blueprint(index, url_prefix='/')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(category, url_prefix='/category')

if __name__ == '__main__':
    app.run()
