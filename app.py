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

import ipyleaflet as L
import datetime
from htmltools import css
from shiny import App, reactive, render, ui
from shinywidgets import output_widget, reactive_read, register_widget

# app_ui = ui.page_fluid(
#     ui.h2("This is iEAT, interactive Ecological Analysis Network"),
#     ui.input_slider("n", "N", 0, 100, 20),
#     ui.output_text_verbatim("txt"),
# )

app_ui = ui.page_fluid(
    ui.h2("This is iEAT, interactive Ecological Analysis Network"),
    ui.h3('---------'),
    ui.h3('Bodemschuifspanning τmax (N/m2) geometrie voorjaar 2021'),
    ui.h3('---------'),
    ui.div(
        ui.input_slider("zoom", "Map zoom level", value=12, min=1, max=18),
        ui.output_ui("map_bounds"),
        style=css(
            display="flex", justify_content="center", align_items="center", gap="2rem"
        ),
    ),
    output_widget("map"),
)

def on_location_changed(event):
    # Do some computation given the new marker location, accessible from `event['new']`
    print(str(datetime.datetime.now()))
    pass

def layerref():
    wms = L.WMSLayer(
    url='http://localhost:8080/geoserver/wms',
    layers='bovenmaas:total_shear_stress_3200',
    format='image/png',
    transparent=True,
    attribution='Bodemschuifspanning')
    return wms


def server(input, output, session):
    # Initialize and display when the session starts (1)
    map = L.Map(center=(51.68356, 5.96274), zoom=16, scroll_wheel_zoom=True)
    # Add a distance scale
    map.add_control(L.leaflet.ScaleControl(position="bottomleft"))
    register_widget("map", map)

    # request for a layer
    wms = layerref()
    map.add_layer(wms)

    # add a click marker
    marker = L.Marker(location=(51.68356, 5.96274), draggable=True)
    map.add_layer(marker)

    # marker can now be moved.
    marker.observe(on_location_changed, 'location')   

    # When the slider changes, update the map's zoom attribute (2)
    @reactive.Effect
    def _():
        map.zoom = input.zoom()

    # When zooming directly on the map, update the slider's value (2 and 3)
    #@reactive.Effect
    #def _():
    #    ui.update_slider("zoom", value=reactive_read(map, "zoom"))

    # Everytime the map's bounds change, update the output message (3)
    @output
    @render.ui
    def map_bounds():
        center = reactive_read(map, "center")
        if len(center) == 0:
            return

        lat = round(center[0], 4)
        lon = (center[1] + 180) % 360 - 180
        lon = round(lon, 4)

        return ui.p(f"Latitude: {lat}", ui.br(), f"Longitude: {lon}")


app = App(app_ui, server)

