from functools import wraps
from flask import request, abort, redirect, url_for
from cmdb.utils.logger import get_logger
from jwcrypto.jwt import JWTExpired, JWTNotYetValid
from jwcrypto.jws import InvalidJWSSignature, InvalidJWSObject
from cmdb.user_management import User, UserRight
LOGGER = get_logger()


def json_required(f):
    @wraps(f)
    def _json_required(*args, **kwargs):
        if not request or not request.json:
            LOGGER.warn("Not json | {}".format(request))
            abort(400)
        return f(*args, **kwargs)
    return _json_required


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'access-token' in request.cookies:
            token = request.cookies.get('access-token')
        else:
            return redirect(url_for('auth_pages.login_page'))
        try:
            from flask import current_app
            security_manager = current_app.manager_holder.get_security_manager()
            security_manager.decrypt_token(token)
        except (JWTExpired, JWTNotYetValid, InvalidJWSSignature, InvalidJWSObject) as e:
            return redirect(url_for('auth_pages.login_page', error=e))
        except Exception as e:
            return redirect(url_for('auth_pages.login_page', error=e))
        return f(*args, **kwargs)
    return decorated


def right_required(required_right: str):
    """
    See Also: https: // stackoverflow.com / questions / 5929107 / decorators -
    with-parameters
        https: // www.artima.com / weblogs / viewpost.jsp?thread = 240845"""

    def page_right(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            from flask import current_app
            user_manager = current_app.manager_holder.get_user_manager()
            right = user_manager.get_right()
            security_manager = current_app.manager_holder.get_security_manager()
            user = User(security_manager.decrypt_token(request.cookies.get('access-token')))
            print(user)
            try:
                user_manager.user_has_right(user, required_right)
            except Exception:
                abort(401)
                return redirect(url_for('static_pages.error_404_page'))
            return f(*args, **kwargs)
        return decorated
    return page_right