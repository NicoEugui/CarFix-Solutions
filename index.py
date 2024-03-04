import os
from src import init_app

configuration = os.getenv('development')
app = init_app(configuration)

if __name__ == '__main__':
    app.run()
