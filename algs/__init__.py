#!../venv/Scripts/python.exe
# -*- encoding : utf-8 -*-

"""
@Description:  This sub-package contains required tools to perform integer factoring.
@Author: Quentin Delamea
@Copyright: Copyright 2020, PyShor
@Credits: [Quentin Delamea]
@License: MIT
@Version: 0.0.1
@Maintainer: Quentin Delamea
@Email: qdelamea@gmail.com
@Status: Dev
"""

from .classicalg import is_prime_number, primer_power, gcd, NotPrimerPowerException
from .quantalg import period_finder
