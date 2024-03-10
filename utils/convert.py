#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Aymeric Lamaallem
# version ='1.0'
# ---------------------------------------------------------------------------
""" Module to add all function to make some conversion """
# ---------------------------------------------------------------------------


def convert_mpers_2_kmperh(value: float) -> float:
    """
    Function to transform a value in m/s into km/h
    Used for:
        * Wind
    """

    return value*3.6
