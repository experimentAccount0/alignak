#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2015: Alignak team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak.
#
# Alignak is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alignak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Alignak.  If not, see <http://www.gnu.org/licenses/>.
#
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#  Copyright (C) 2009-2014:
#     Hartmut Goebel, h.goebel@goebel-consult.de
#     Nicolas Dupeux, nicolas@dupeux.net
#     Grégory Starck, g.starck@gmail.com
#     Sebastien Coavoux, s.coavoux@free.fr
#     Thibault Cohen, titilambert@gmail.com
#     Jean Gabes, naparuba@gmail.com
#     Zoran Zaric, zz@zoranzaric.de

#  This file is part of Shinken.
#
#  Shinken is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Shinken is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Shinken.  If not, see <http://www.gnu.org/licenses/>.
"""Brok module provide Brok class which is basically event for Alignak.
Brok are filled depending on their type (check_result, initial_state ...)

"""
import cPickle


class Brok:
    """A Brok is a piece of information exported by Alignak to the Broker.
    Broker can do whatever he wants with it.
    """
    __slots__ = ('__dict__', 'id', 'type', 'data', 'prepared', 'instance_id')
    id = 0
    my_type = 'brok'

    def __init__(self, type, data):
        self.type = type
        self.id = self.__class__.id
        self.__class__.id += 1
        self.data = cPickle.dumps(data, cPickle.HIGHEST_PROTOCOL)
        self.prepared = False

    def __str__(self):
        return str(self.__dict__) + '\n'

    def prepare(self):
        """Unpickle data from data attribute and add instance_id key if necessary

        :return: None
        """
        # Maybe the brok is a old daemon one or was already prepared
        # if so, the data is already ok
        if hasattr(self, 'prepared') and not self.prepared:
            self.data = cPickle.loads(self.data)
            if hasattr(self, 'instance_id'):
                self.data['instance_id'] = self.instance_id
        self.prepared = True