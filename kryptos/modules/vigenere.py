#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 2023

@author: iluzioDev
@project: kryptos
@file: vigenere.py

@description: Vigenere cipher
"""
from .cipher import Cipher

class Vigenere(Cipher):
  """
  Vigenere cipher class.

  The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages. It operates by shifting the characters of the plaintext based on the corresponding letters of the keyword. The cipher provides stronger encryption compared to simple substitution ciphers, as it introduces variability in the shifting pattern.
  """
  @staticmethod
  def encrypt(message, key):
    """
    Encrypts a message
    """
    return Vigenere.__crypt(message, key, True)

  @staticmethod
  def decrypt(message, key):
    """
    Decrypts a message
    """
    return Vigenere.__crypt(message, key, False)

  @staticmethod
  def __crypt(message, key, encrypt):
    """
    Crypts a message using Vigenere cipher
    """
    result = []
    crypted_message = str()
    message = message.split(" ")
    i = 0
    for word in message:
      for char in word:
        char_index = Vigenere.ALPHABET.index(char.upper())
        key_index = Vigenere.ALPHABET.index(key[i % len(key)].upper())
        i += 1
        if char.upper() in Vigenere.ALPHABET:
          if encrypt:
            crypted_message += Vigenere.ALPHABET[(char_index + key_index) % len(Vigenere.ALPHABET)]
          else:
            crypted_message += Vigenere.ALPHABET[(char_index - key_index) % len(Vigenere.ALPHABET)]
        else:
          crypted_message += char
      result.append(crypted_message)
      crypted_message = str()
    return " ".join(result)
