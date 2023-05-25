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
from .utils import split_by, parseHex, bitwise_shift, truncate
from .cipher import Cipher

class ChaCha20(Cipher):
  """
  ChaCha20 cipher class

  ChaCha20 is a stream cipher designed by Daniel J. Bernstein that has been
  proposed as a standard by the Internet Engineering Task Force (IETF).
  It is a refinement of the Salsa20 algorithm, offering better security and
  performance than Salsa20.
  """
  ROUNDS = 10
  CONSTANT = split_by(parseHex('61707865:3320646E:79622D32:6B206574'), 8)
  BITS = 32
  HEX = int(BITS / 4)
  WORDS = 16
  
  def encrypt(self, message, key, counter, nonce):
    return self.__crypt(message, key, counter, nonce)
  
  def __crypt(self, message, key, counter, nonce):
    return
  
  def __quarter_round(self, a, b, c, d):
    try:
      a = truncate(a + b, self.HEX)
      d = bitwise_shift(d ^ a, 16, self.BITS, self.HEX)
      c = truncate(c + d, self.HEX)
      b = bitwise_shift(b ^ c, 12, self.BITS, self.HEX)
      a = truncate(a + b, self.HEX)
      d = bitwise_shift(d ^ a, 8, self.BITS, self.HEX)
      c = truncate(c + d, self.HEX)
      b = bitwise_shift(b ^ c, 7, self.BITS, self.HEX)
      
      return a, b, c, d
    except ValueError as exception:
      raise exception
    
