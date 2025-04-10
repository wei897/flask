from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'some_secret_key_for_development'

# 模拟数据库
tasks = [
    {'id': 1, 'title': '学习 Flask', 'done': False},
    {'id': 2, 'title': '构建 Web 应用', 'done': False},
    {'id': 3, 'title': '部署应用', 'done': False}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        # 生成新的 ID (在实际应用中会由数据库生成)
        new_id = max([task['id'] for task in tasks]) + 1 if tasks else 1
        tasks.append({'id': new_id, 'title': title, 'done': False})
        flash('任务已添加!')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            status = '完成' if task['done'] else '未完成'
            flash(f'任务 "{task["title"]}" 标记为{status}!')
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            flash(f'任务 "{tasks.pop(i)["title"]}" 已删除!')
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
