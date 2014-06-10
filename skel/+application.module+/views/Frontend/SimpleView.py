# -*- coding: utf-8 -*-
# {{{ application.name }}}
# {{{ author.name }}}

import flask, json, logging, os
import flask.ext.security as security

simpleview = flask.Blueprint('simpleview', __name__, template_folder='templates', static_folder='static')

@simpleview.route('/')
def index():
    return flask.redirect(flask.url_for(".simple"))

@simpleview.route('/simple')
def simple():
    return flask.render_template('simple.html')
