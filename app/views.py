from app import flask_app
from flask import request, render_template
from tasks import add_together

@flask_app.route('/')
def index():
    return 'Hello, World2!'

# Example route
@flask_app.route('/example')
def example():
    return 'This is an example route'

# Example route
@flask_app.get('/hello_world')
def hello_world():
    return render_template('hello_world.html')



@flask_app.post("/add")
def start_add() -> dict[str, object]:
    a = request.form.get("a", type=int)
    b = request.form.get("b", type=int)
    result = add_together.delay(a, b)
    return {"result_id": result.id}

from celery.result import AsyncResult

@flask_app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }

@flask_app.route('/add_together', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        result = a + b
        return render_template('result.html', result=result)
    return render_template('form.html')

# if __name__ == '__main__':
#     app.run()