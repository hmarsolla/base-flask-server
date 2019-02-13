
import config
import my_api
from waitress import serve

serve(my_api.create_app(config), host='0.0.0.0', port=config.PORT)