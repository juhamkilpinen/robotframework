#  Copyright 2008-2009 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from robot.errors import DataError


class BaseHandler:

    def __getattr__(self, name):
        if name == 'longname':
            return '%s.%s' % (self.library.name, self.name)
        if name == 'shortdoc':
            return self.doc and self.doc.splitlines()[0] or ''
        raise AttributeError("%s does not have attribute '%s'"
                             % (self.__class__.__name__, name))

    def _tracelog_args(self, logger, posargs, kwargs={}):
        logger.trace('Arguments: %s %s' % (posargs, kwargs))


class UserErrorHandler:
    """Created if creating handlers fail -- running raises DataError.

    The idea is not to raise DataError at processing time and prevent all
    tests in affected test case file from executing. Instead UserErrorHandler
    is created and if it is ever run DataError is raised then.
    """
    type = 'error'

    def __init__(self, name, error):
        self.name = self.longname = name
        self.doc = self.shortdoc = ''
        self._error = error
        self.timeout = ''

    def run(self, *args):
        raise DataError(self._error)
