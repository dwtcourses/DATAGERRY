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

from cmdb.exportd.exportd_job.exportd_job_base import JobManagementBase
from enum import Enum
from cmdb.framework.cmdb_dao import CmdbDAO

try:
    from cmdb.utils.error import CMDBError
except ImportError:
    CMDBError = Exception


class ExecuteState(Enum):
    SUCCESSFUL = 0
    INFO = 1
    WARNING = 2
    FAILED = 3
    RUNNING = 4


class ExportdJobType(Enum):
    PUSH = 0
    PULL = 1


class ExportdJob(JobManagementBase):
    """
        Exportd Job
    """
    COLLECTION = 'exportd.jobs'
    REQUIRED_INIT_KEYS = [
        'name',
    ]

    INDEX_KEYS = [
        {'keys': [('name', CmdbDAO.DAO_ASCENDING)], 'name': 'name', 'unique': True}
    ]

    def __init__(self, name, label, description, active, author_id,
                 last_execute_date, sources, destination,
                 variables, scheduling, exportd_type=ExportdJobType.PUSH.name, state=None, **kwargs):
        """
        Args:
            name: name of this job
            active: is job executable
            sources: consists of multiple objects of a specific object type and a specific status
            destination: is an external system, where you want to push the yourcmdb objects
            variables: has a name and gets its value out of fields of the objects
            **kwargs: optional params
        """
        self.name = name
        self.label = label
        self.description = description
        self.active = active
        self.author_id = author_id
        self.last_execute_date = last_execute_date
        self.sources = sources
        self.destination = destination
        self.variables = variables
        self.scheduling = scheduling
        self.state = state or 0
        self.exportd_type = exportd_type or ExportdJobType.PUSH.name
        super(ExportdJob, self).__init__(**kwargs)

    def get_public_id(self) -> int:
        """
        get the public id of current element

        Note:
            Since the dao object is not initializable
            the child class object will inherit this function
            SHOULD NOT BE OVERWRITTEN!

        Returns:
            int: public id

        Raises:
            NoPublicIDError: if `public_id` is zero or not set

        """
        if self.public_id == 0 or self.public_id is None:
            raise NoPublicIDError()
        return self.public_id

    def get_name(self) -> str:
        """
        Get the name of the job
        Returns:
            str: display name
        """
        if self.name is None:
            return ""
        else:
            return self.name

    def get_label(self) -> str:
        """
        Get the label of the job
        Returns:
            str: display label
        """
        if self.label is None:
            return ""
        else:
            return self.label

    def get_active(self) -> bool:
        """
        Get active state of the job
        Returns:
            bool: is job executable
        """
        if self.active is None:
            return ""
        else:
            return self.active

    def get_sources(self):
        """
        Get all sources of the job
        Returns:
            list: all sources
        """
        return self.sources

    def get_destinations(self):
        """
        Get all destinations of the job
        Returns:
            list: all destinations
        """
        return self.destination

    def get_variables(self):
        """
        Get all variables of the job
        Returns:
            list: all variables
        """
        return self.variables

    def get_scheduling(self):
        """
        Get scheduling of the job
        Returns:
            list: all scheduling
        """
        return self.scheduling

    def get_state(self):
        """
        Get state of executation of the job
        Returns:
            str:
        """
        return self.state

    def get_exportd_typ(self):
        """
        Get type of executation of the job
        Returns:
            str:
        """
        return self.exportd_type

    def get_author_id(self):
        return self.author_id


class NoPublicIDError(CMDBError):
    """
    Error if object has no public key and public key was'n removed over IGNORED_INIT_KEYS
    """

    def __init__(self):
        super().__init__()
        self.message = 'The object has no general public id - look at the IGNORED_INIT_KEYS constant or the docs'