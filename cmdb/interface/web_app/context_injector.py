from cmdb.interface.web_app import MANAGER_HOLDER


def inject_object_manager():
    def object_manager():
        return MANAGER_HOLDER.get_object_manager()

    return dict(object_manager=object_manager())


def inject_sidebar():
    def sidebar():
        categories = MANAGER_HOLDER.get_object_manager().get_all_categories()
        return categories
    return dict(sidebar=sidebar())


def inject_sidebar_hidden():
    def sidebar_hidden():
        import flask
        if 'sidebar_hidden' in flask.request.cookies:
            return True
        return False
    return dict(sidebar_hidden=sidebar_hidden())


def inject_current_url():
    def current_url():
        from flask import request
        return request.base_url

    return dict(current_url=current_url)