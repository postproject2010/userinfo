from environs import Env

env = Env()
env.read_env()

API_TOKEN = env('API_TOKEN')
ADMIN = env('ADMIN')

