# -*- coding: utf-8 -*-

#  Copyright (C) 2019-2022 Adrian Polyakov
#
#  This file is part of VkMusic Downloader
#
#  VkMusic Downloader is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see http://www.gnu.org/licenses/
from PyInstaller.utils.hooks import collect_submodules, copy_metadata

hiddenimports = collect_submodules('keyring.backends')
datas = copy_metadata('keyring')