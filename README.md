<h1 align="center">Getting things done</h1>
<p align="center"><img src="images/todo.png" width=650px></p>
<h1 align="center">Manage and track your daily tasks</h1>
<p>This app is as simple as to-do list apps come. It’s a gorgeously minimal app that does exactly what it’s supposed to and no more. You can create tasks, update, delete, mark tasks with done - undone, set priority, filter by priority and move tasks up or down.</p>
<h2>Demo</h2>
  <img src="images/demo.png">
<h2>Getting started</h2>
<p>Clone the source locally:</p>
<pre> 
      $ git clone https://github.com/alexshchegretsov/TODO_manager.git
      $ cd TODO_manager
</pre>
<p>Update package list and install pip for Python 3:</p>
<pre>
      $ sudo apt update
      $ sudo apt install python3-pip
</pre>
<p>Once the installation is complete, verify the installation by checking the pip version:</p>
<pre>
      $ pip3 --version
</pre>
<p>You are still at /TODO_manager/ directory, create and run virtual environment:</p>
<pre>
      $ virtualenv -p python3.7 .venv
      $ source .venv/bin/activate
</pre>
<h4>Install all dependencies from requirements.txt:</h4>
<pre>
      $ pip3 install -r requirements.txt
</pre>
<p>Move to /src/ directory and run server:</p>
<pre>
      $ cd src/
      $ ./manage.py runserver
</pre>
<p>Open your browser in a new window and go to localhost, for this you need to enter in the input line:</p>
<pre>
      http://127.0.0.1:8000/
</pre>
<h2>Built with</h2>
<ul>
  <li><a href="https://www.djangoproject.com/">Django</a> - The web framework used</li>
  <li><a href="https://milligram.io/">Milligram</a> - A minimalist CSS framework</li>
</ul>
<h2>License</h2>
<p>MIT &copy; <a href="https://github.com/alexshchegretsov">Alex Shchegretsov</a></p>
