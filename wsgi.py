import os

# Heroku/Gunicorn entrypoint for Flask
# This imports the Flask instance named `app` from src/app.py
os.environ.setdefault("PYTHONUNBUFFERED", "1")

MODULE_NAME = "src.app"   # your Flask module path
APP_VAR = "app"           # the Flask instance variable in that module

mod = __import__(MODULE_NAME, fromlist=[APP_VAR])
app = getattr(mod, APP_VAR)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
