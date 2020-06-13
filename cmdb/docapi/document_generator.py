# DATAGERRY - OpenSource Enterprise CMDB
# Copyright (C) 2019 NETHINKS GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import jinja2

from cmdb.templates.template_data import ObjectTemplateData

class DocumentGenerator:

    def generate_doc():
        pass


class ObjectDocumentGenerator:

    def __init__(self, template, object_manager, cmdb_object, doctype):
        self.__template = template
        self.__object_manager = object_manager
        self.__cmdb_object = cmdb_object
        self.__doctype = doctype

    def generate_doc(self):
        # ToDo: error handling
        template_data = ObjectTemplateData(self.__object_manager, self.__cmdb_object).get_template_data()
        template = jinja2.Template(self.__template.get_template_data())
        rendered_template = template.render(template_data)

        # create document
        return self.__doctype.create_doc(rendered_template)