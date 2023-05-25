#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 2023

@author: iluzioDev
@project: kryptos
@file: chacha20.py

@description: ChaCha20 cipher
"""
import simple_chalk as chalk
from .cipher import Cipher

class ChaCha20(Cipher):
  """
  ChaCha20 cipher class

  ChaCha20 is a stream cipher designed by Daniel J. Bernstein that has been
  proposed as a standard by the Internet Engineering Task Force (IETF).
  It is a refinement of the Salsa20 algorithm, offering better security and
  performance than Salsa20.
  """
  def __crypt(self, message, key, counter, nonce):
    return
  
