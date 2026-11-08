from backend.app import app


if _name_ == "_main_":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)