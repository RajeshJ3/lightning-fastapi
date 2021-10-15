import uvicorn

from api.settings import app, app_config
from api.helpers import prepare_routes

prepare_routes()

if __name__ == '__main__':
    uvicorn.run(app, **app_config)
