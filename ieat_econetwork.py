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


def getspecies_velocity(velocity):
    """
    This is a first attempt to show the effect of physical characteristics on species
    TODO is setting up ecological network, for now 1 species and 1 stress factor are used
    Data for species and velocity is derived from KRW habitat tables

    returns yes no for a species

    Parameters
    velocity: Double

    Return
    boolean
    """

    # dctspecies is a dictionary with species and upper and lower boundary
    dctspecies = {}
    dctspecies["Barbeel"] = (0.05, 1)
    dctspecies["Atlantische zalm"] = (1, 5)
    dctspecies["Atlantische steur"] = (1, 5)
    dctspecies["elft"] = (0.05, 5)

    species = "Barbeel"
    velocity = velocity / 10
    vals = dctspecies[species]
    res = False if velocity < vals[0] else False if velocity >= vals[1] else True
    return res
