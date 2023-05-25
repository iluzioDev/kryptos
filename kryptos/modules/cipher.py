#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 2023

@author: iluzioDev
@project: kryptos
@file: cipher.py

@description: Base cipher
"""
from .singleton import Singleton

class Cipher(metaclass = Singleton):
  """
  Base cipher class that defines the methods that every complex cipher must have
  """
  ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  def __init__(self):
    """
    Constructor of the class
    """
    self._debug = False
    
  def encrypt(self, *args):
    """
    Encrypts a message
    """
    
  def decrypt(self, *args):
    """
    Decrypts a message
    """
    
  def __crypt(self, *args):
    """
    Crypts a message
    """
  
  def enable_debug(self):
    """
    Enables the test mode for debugging purposes
    """
    self._debug = True
    return self._debug
