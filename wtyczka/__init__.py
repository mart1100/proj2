# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka
                                 A QGIS plugin
 wtyczka
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-03
        copyright            : (C) 2024 by sss
        email                : ads
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load wtyczka class from file wtyczka.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .wtyczka import wtyczka
    return wtyczka(iface)
