# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

css = Bundle(
    "libs/bootstrap/dist/css/paper/bootstrap.css",
    "css/style.css",
    "css/bootstrap-markdown.min.css",
    filters="cssmin",
    output="public/css/common.css"
)

js = Bundle(
    "libs/jQuery/dist/jquery.js",
    "libs/bootstrap/dist/js/bootstrap.js",
    "js/bootstrap-markdown.js",
    "js/plugins.js",
    filters='jsmin',
    output="public/js/common.js"
)

fonts = Bundle()
assets = Environment()

assets.register("js_all", js)
assets.register("css_all", css)
