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

import pandas as pd


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

    fb = []
    for sp in dctspecies.keys():
        velocity = velocity / 50
        vals = dctspecies[sp]
        res = False if velocity < vals[0] else False if velocity >= vals[1] else True
        fb.append((sp, res))
        # print(sp, res)

    df = pd.DataFrame(fb, columns=["fish", "occurence"])
    return fb, df


def testing():
    atxt = ""
    species = getspecies_velocity(15.2)
    for i in range(len(species)):
        atxt = atxt + "\n" + species[i][0] + " " + str(species[i][1])
    print(atxt)
    atxt = f"{species}".strip("[]")

    print(atxt)


def heatmap():
    """
    actions== install numpy and seaborn
    https://www.statology.org/heatmap-python/
    """

    import numpy as np
    import pandas as pd
    import seaborn as sns

    # create a dataset
    np.random.seed(0)
    data = {
        "day": np.tile(["Mon", "Tue", "Wed", "Thur", "Fri"], 5),
        "week": np.repeat([1, 2, 3, 4, 5], 5),
        "sales": np.random.randint(0, 50, size=25),
    }

    df = pd.DataFrame(data, columns=["day", "week", "sales"])
    df = df.pivot(index="day", columns="week", values="sales")
    sns.heatmap(df)

    np.random.seed(0)
    data = {
        "species": np.tile(["Barbeel", "Atlantische zalm", "Atlantische steur"], 3),
        "voorkomen": np.repeat([1, 0, 1], 3),
        "waarde": np.random.randint(0, 1, size=9),
    }
    df = pd.DataFrame(data, columns=["species", "voorkomen", "waarde"])
    df = df.pivot(index="species", columns="voorkomen", values="waarde")
    sns.heatmap(df)
