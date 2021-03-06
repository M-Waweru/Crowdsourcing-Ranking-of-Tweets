# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2015 SciFabric LTD.
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa. If not, see <http://www.gnu.org/licenses/>.

import enki
import json
import settings

def basic(**kwargs):
    """A basic analyzer."""
    e = enki.Enki(endpoint=settings.endpoint,
                  api_key=settings.api_key,
                  project_short_name=kwargs['project_short_name'])
    e.get_tasks(task_id=kwargs['task_id'])
    e.get_task_runs()
    for t in e.tasks: # pragma: no cover
        desc = e.task_runs_df[t.id]['info'].describe()
        # print "The top answer for task.id %s is %s" % (t.id, desc['top'])
        value_counts = e.task_runs_df[t.id]['info'].value_counts()
        analysis = dict(value_counts)
        summary = dict(desc)
        result = enki.pbclient.find_results(project_id=kwargs['project_id'],
                                            id=kwargs['result_id'])[0]
        result.info = dict(summary=summary, analysis=analysis)
        enki.pbclient.update_result(result)
    with open('./static/results.json', 'w') as f:
        f.write(json.dumps(kwargs))
    return "OK"

def checkBBI():
    e = enki.Enki(api_key='c25db137-bde1-4d86-ae4b-f71e928395db', endpoint='http://waturanknews.live',                  
                project_short_name='checkBBI',
                all=1)

    e.get_all()
    tasks_info = {}

    for t in e.tasks:
        desc = e.task_runs_df[t.id]['info'].describe()
        value_counts = e.task_runs_df[t.id]['info'].value_counts()
        analysis = dict(value_counts)
        summary = dict(desc)

        tasks_info[t.id] = analysis, summary

    return tasks_info
    

    
