import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from flask import *
app = Flask(__name__)

active_list = []
inactive_list = []

@app.route("/")
def index():
    num_active = len(active_list)
    num_inactive = len(inactive_list)
    return render_template('index.html',active_list=active_list,
            inactive_list=inactive_list,num_active=num_active,num_inactive=num_inactive)

@app.route("/add", methods=['POST'])
def add():
    new_task = request.form['task']
    active_list.append(new_task)
    return redirect('/')

@app.route("/complete", methods=['POST'])
def complete():
    to_complete = request.form['task']
    if to_complete in active_list:
        active_list.remove(to_complete)
    inactive_list.append(to_complete)
    return redirect('/')

@app.route("/clear", methods=['POST'])
def clear():
    inactive_list.clear()
    return redirect('/')

@app.route("/pie.png")
def pie():
    plt.clf()
    labels = 'Incomplete', 'Complete'
    sizes = [len(active_list), len(inactive_list)]
    colors = ['red', 'green']
    plt.pie(sizes, labels=labels, colors=colors)
    plt.savefig('pie.png')
    return send_file('pie.png', cache_timeout=0)

if __name__ == "__main__":
    app.run()
