from main import app, ok
from services.news.app import news

# TODO: /api prefix must be a generic place to applied for all routes 
app.register_blueprint(news, url_prefix="/api/news")


@app.route("/healthcheck")
def healthcheck():
    return ok(data="healthcheck successfull", code=200)