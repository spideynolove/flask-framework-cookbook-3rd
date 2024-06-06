# Add new templates 

## Jinja 1'st sample

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seeking Alpha Mockup</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <!-- Add any other necessary CSS links here -->
</head>
<body>
    <nav class="navbar">
        <div class="navbar-brand">
            <h1>Seeking Alpha</h1>
        </div>
        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <span>No username</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="sidebar">
        <ul>
            <li><a href="#">Upgrade To Premium</a></li>
            <li><a href="#">About Premium</a></li>
            <li><a href="#">Explore Alpha Picks</a></li>
            <li><a href="#">Home</a></li>
            <li><a href="#">Analysis</a></li>
            <li><a href="#">News</a></li>
            <li><a href="#">Market Data</a></li>
            <li><a href="#">Explore Investing Groups</a></li>
        </ul>
    </div>

    <div class="bottom-nav">
        <ul>
            <li><a href="#">Portfolio</a></li>
            <li><a href="#">Ideas</a></li>
            <li><a href="#">News</a></li>
            <li><a href="#">Markets</a></li>
            <li><a href="#">More</a></li>
        </ul>
    </div>

    <!-- Add your main content here -->

    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
    <!-- Add any other necessary JS links here -->
</body>
</html>
```

### stylesheet 

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.navbar {
    background-color: #000;
    color: #fff;
    display: flex;
    justify-content: space-between;
    padding: 1rem;
}

.navbar-brand h1 {
    margin: 0;
}

.navbar-menu .navbar-end .navbar-item {
    color: #fff;
}

.sidebar {
    background-color: #333;
    color: #fff;
    height: 100vh;
    padding: 1rem;
    position: fixed;
    width: 200px;
}

.sidebar ul {
    list-style-type: none;
    padding: 0;
}

.sidebar ul li {
    margin: 1rem 0;
}

.sidebar ul li a {
    color: #fff;
    text-decoration: none;
}

.sidebar ul li a:hover {
    text-decoration: underline;
}

.bottom-nav {
    background-color: #000;
    bottom: 0;
    color: #fff;
    display: flex;
    justify-content: space-around;
    padding: 1rem 0;
    position: fixed;
    width: 100%;
}

.bottom-nav ul {
    display: flex;
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 100%;
    justify-content: space-around;
}

.bottom-nav ul li a {
    color: #fff;
    text-decoration: none;
}

.bottom-nav ul li a:hover {
    text-decoration: underline;
}
```

## Jinja 2nd samples

### base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Seeking Alpha Mockup{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <nav class="navbar">
        <div class="navbar-brand">
            <h1>Seeking Alpha</h1>
        </div>
        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <span>No username</span>
                </div>
            </div>
        </div>
    </nav>

    <div class="sidebar">
        <ul>
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('upgrade') }}">Upgrade To Premium</a></li>
            <li><a href="{{ url_for('about_premium') }}">About Premium</a></li>
            <li><a href="{{ url_for('alpha_picks') }}">Explore Alpha Picks</a></li>
            <li><a href="{{ url_for('analysis') }}">Analysis</a></li>
            <li><a href="{{ url_for('news') }}">News</a></li>
            <li><a href="{{ url_for('market_data') }}">Market Data</a></li>
            <li><a href="{{ url_for('investing_groups') }}">Explore Investing Groups</a></li>
        </ul>
    </div>

    <div class="content">
        {% block content %}
        {% endblock %}
    </div>

    <div class="bottom-nav">
        <ul>
            <li><a href="{{ url_for('portfolio') }}">Portfolio</a></li>
            <li><a href="{{ url_for('ideas') }}">Ideas</a></li>
            <li><a href="{{ url_for('news') }}">News</a></li>
            <li><a href="{{ url_for('markets') }}">Markets</a></li>
            <li><a href="{{ url_for('more') }}">More</a></li>
        </ul>
    </div>

    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
</body>
</html>
```

### home.html

```html
{% extends 'base.html' %}

{% block title %}Home - Seeking Alpha{% endblock %}

{% block content %}
    <h2>Welcome to Seeking Alpha</h2>
    <p>This is the homepage content.</p>
    <!-- Add specific content here -->
{% endblock %}
```

### news.html

```html
{% extends 'base.html' %}

{% block title %}News - Seeking Alpha{% endblock %}

{% block content %}
    <h2>News</h2>
    <div class="news-list">
        <div class="news-item">
            <h3>Investors show pessimism as focus shifts to latest economic data</h3>
            <p>SP500 -0.01% Now!</p>
        </div>
        <div class="news-item">
            <h3>Devon missed energy deal wave as acquisition targets were skeptical - Reuters</h3>
            <p>DVN -0.54% Now!</p>
        </div>
        <div class="news-item">
            <h3>Franklin Templeton said to explore launching new private crypto fund</h3>
            <p>BEN -0.43% Now!</p>
        </div>
    </div>
{% endblock %}
```

### stylesheet 

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.navbar {
    background-color: #000;
    color: #fff;
    display: flex;
    justify-content: space-between;
    padding: 1rem;
}

.navbar-brand h1 {
    margin: 0;
}

.navbar-menu .navbar-end .navbar-item {
    color: #fff;
}

.sidebar {
    background-color: #333;
    color: #fff;
    height: 100vh;
    padding: 1rem;
    position: fixed;
    width: 200px;
}

.sidebar ul {
    list-style-type: none;
    padding: 0;
}

.sidebar ul li {
    margin: 1rem 0;
}

.sidebar ul li a {
    color: #fff;
    text-decoration: none;
}

.sidebar ul li a:hover {
    text-decoration: underline;
}

.content {
    margin-left: 220px;
    padding: 20px;
}

.bottom-nav {
    background-color: #000;
    bottom: 0;
    color: #fff;
    display: flex;
    justify-content: space-around;
    padding: 1rem 0;
    position: fixed;
    width: 100%;
}

.bottom-nav ul {
    display: flex;
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 100%;
    justify-content: space-around;
}

.bottom-nav ul li a {
    color: #fff;
    text-decoration: none;
}

.bottom-nav ul li a:hover {
    text-decoration: underline;
}

.news-list {
    display: flex;
    flex-direction: column;
}

.news-item {
    background: #444;
    color: #fff;
    margin-bottom: 1rem;
    padding: 1rem;
}
```

### Flask app

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/news')
def news():
    return render_template('news.html')

# Add other routes here

if __name__ == '__main__':
    app.run(debug=True)
```

