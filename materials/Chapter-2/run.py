from my_app import app
import locale

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


def intcomma(value):
    return locale.format_string("%d", value, grouping=True)


app.jinja_env.filters["intcomma"] = intcomma
app.run(debug=True)
