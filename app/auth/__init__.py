from unicodedata import name
from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views