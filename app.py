from flask import Flask
from flask_cors import CORS

from repository.core.ai.luna import Luna

# Loading Luna AI
luna = Luna()


def create_app():
    # Starting Flask app
    flask_app = Flask(__name__)
    # Adding cors validation for external api calls
    CORS(flask_app)

    from controller.routes.luna_routes_controller import luna_routes_controller_bp
    flask_app.register_blueprint(luna_routes_controller_bp)

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
