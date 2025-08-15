from bot import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port or default 5000
    app.run(host='0.0.0.0', port=port, debug=True)
