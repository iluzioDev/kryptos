#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 2023

@author: iluzioDev
@project: kryptos
@file: singleton.py

@description: Singleton metaclass
"""
class Singleton(type):
  """
  Metaclass for creating singleton classes
  """
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super().__call__(*args, **kwargs)
    return cls._instances[cls]
