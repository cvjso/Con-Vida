import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '3hf8928yhg947238jeh98qdj398487h928r3389gfhfw7398quj8' # Chave para segurança

from application.api import controller