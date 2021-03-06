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

import logging

from cmdb.importer.parser_response import ParserResponse, ObjectParserResponse

LOGGER = logging.getLogger(__name__)
try:
    from cmdb.utils.error import CMDBError
except ImportError:
    CMDBError = Exception


class BaseParser:
    DEFAULT_CONFIG = {}

    def __new__(cls, *args, **kwargs):
        return super(BaseParser, cls).__new__(cls)

    def __init__(self, parser_config: dict = None):
        _parser_config = parser_config or self.DEFAULT_CONFIG
        self.parser_config: dict = {**self.DEFAULT_CONFIG, **_parser_config}

    def get_config(self) -> dict:
        return self.parser_config

    def parse(self, file) -> ParserResponse:
        raise NotImplementedError


class BaseObjectParser(BaseParser):
    DEFAULT_CONFIG = {}

    def __init__(self, parser_config: dict):
        super(BaseObjectParser, self).__init__(parser_config)

    def parse(self, file) -> ObjectParserResponse:
        raise NotImplementedError


class BaseTypeParser(BaseParser):
    DEFAULT_CONFIG = {}

    def __init__(self, parser_config: dict):
        super(BaseTypeParser, self).__init__(parser_config)

    def parse(self, file) -> ObjectParserResponse:
        raise NotImplementedError
