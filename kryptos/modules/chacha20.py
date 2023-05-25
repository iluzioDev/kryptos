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
from .utils import split_by, to_hex, left_rotate_n_bits, truncate
from .cipher import Cipher

class ChaCha20(Cipher):
  """
  ChaCha20 cipher class

  ChaCha20 is a stream cipher designed by Daniel J. Bernstein that has been
  proposed as a standard by the Internet Engineering Task Force (IETF).
  It is a refinement of the Salsa20 algorithm, offering better security and
  performance than Salsa20.
  """
  # Constants
  ROUNDS = 10
  CONSTANT = split_by(to_hex('61707865:3320646E:79622D32:6B206574'), 8)
  N_BITS = 32
  N_HEX = int(N_BITS / 4)
  N_WORDS = 16
  
  def encrypt(self, message, key, counter, nonce):
    return self.__crypt(message, key, counter, nonce)
  
  def __crypt(self, message, key, counter, nonce):
    return
  
  def __quarter_round(self, a, b, c, d):
    a = truncate(a + b, self.N_HEX)
    d = left_rotate_n_bits(d ^ a, 16, self.N_BITS, self.N_HEX)
    c = truncate(c + d, self.N_HEX)
    b = left_rotate_n_bits(b ^ c, 12, self.N_BITS, self.N_HEX)
    a = truncate(a + b, self.N_HEX)
    d = left_rotate_n_bits(d ^ a, 8, self.N_BITS, self.N_HEX)
    c = truncate(c + d, self.N_HEX)
    b = left_rotate_n_bits(b ^ c, 7, self.N_BITS, self.N_HEX)
    return a, b, c, d
