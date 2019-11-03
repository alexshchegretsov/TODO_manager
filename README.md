<h1 align="center">Getting things done</h1>
<p align="center"><img src="images/todo.png" width=650px></p>
<h1 align="center">Manage and track your daily tasks</h1>
<p>This app is as simple as to-do list apps come. It’s a gorgeously minimal app that does exactly what it’s supposed to and no more. You can create tasks, update, delete, mark tasks with done - undone, set priority, filter by priority and move tasks up or down.</p>
<h2>Demo</h2>
  <img src="images/demo.png">
<h2>Getting started</h2>

<h2>How to run</h2>
<p>Clone the source locally:</p>
<pre> 
      $ git clone https://github.com/alexshchegretsov/TODO_manager.git
      $ cd TODO_manager
</pre>

<p>Run containers with `docker-compose` tool:</p>
<pre>
      $ docker-compose up -d
</pre>
<p>Initialize postgres and collect staticfiles:</p>
<pre>
      $ docker-compose run --rm web ./manage.py migrate
      $ docker-compose run --rm web ./manage.py collectstatic    (type "yes")
</pre>


<p>Open your browser in a new window and go to localhost on 8000 port:</p>
<pre>
      http://127.0.0.1:8000/
</pre>

<h2>Built with</h2>
<ul>
  <li><a href="https://www.djangoproject.com/">Django</a> - The web framework used</li>
  <li><a href="https://milligram.io/">Milligram</a> - A minimalist CSS framework</li>
</ul>
<h2>License</h2>
<p>FREE &copy; <a href="https://github.com/alexshchegretsov">Alex Shchegretsov</a></p>
