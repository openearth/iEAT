 # -*- coding: utf-8 -*-
# Copyright notice
#   --------------------------------------------------------------------
#   Copyright (C) 2023 Deltares
#       Gerrit Hendriksen
#
#   This library is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this library.  If not, see <http://www.gnu.org/licenses/>.
#   --------------------------------------------------------------------
#
# This tool is part of <a href="http://www.OpenEarth.eu">OpenEarthTools</a>.
# OpenEarthTools is an online collaboration to share and manage data and
# programming tools in an open source, version controlled environment.
# Sign up to recieve regular updates of this function, and to contribute
# your own tools.

import json
from owslib.wfs import WebFeatureService
from owslib.wms import WebMapService

wfs11 = WebFeatureService(url='http://localhost:8080/geoserver/wfs', version='1.1.0')
layers='bovenmaas:total_shear_stress_3200'

wms = WebMapService(url='http://localhost:8080/geoserver/wms', version='1.1.1')
list(wms.contents)
layer = 'bovenmaas:total_shear_stress_3200'

def test():
    point = (198541, 403313)
    print(getdata(point))

def getdata(point):
    size = 1
    bbox = (
                point[0] - size,
                point[1] - size,
                point[0] + size,
                point[1] + size,
            )
    _options = {
        'layers': [layer],
        'srs': 'EPSG:28992',
        'bbox': bbox,
        'size': (3, 3),
        #'format': 'image/jpeg',
        'format': "application/json",
        'query_layers': [layer],
        #'info_format': "text/xml",
        'info_format': "application/json",
        'xy': (1, 1)
    }

    response = wms.getfeatureinfo(**_options)
    rsjson = json.loads(response.read())
    tau = rsjson['features'][0]['properties']['mesh2d_tau']
    return tau 