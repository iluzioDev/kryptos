#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 2023

@author: iluzioDev
@project: kryptos
@file: vigenere.py

@description: Vigenere cipher
"""
import simple_chalk as chalk
from .cipher import Cipher

class Vigenere(Cipher):
  """
  Vigenere cipher class.

  The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages. It operates by shifting the characters of the plaintext based on the corresponding letters of the keyword. The cipher provides stronger encryption compared to simple substitution ciphers, as it introduces variability in the shifting pattern.
  """
  def encrypt(self, message, key):
    return self.__crypt(message, key, True)

  def decrypt(self, message, key):
    return self.__crypt(message, key, False)

  def __crypt(self, message, key, encrypt):
    result = []
    crypted_message = str()
    message = message.split(" ")
    i = 0
    for word in message:
      for char in word:
        new_char = char
        if char.upper() in Vigenere.ALPHABET:
          char_index = Vigenere.ALPHABET.index(char.upper())
          key_index = Vigenere.ALPHABET.index(key[i % len(key)].upper())
          if encrypt:
            new_char = Vigenere.ALPHABET[(char_index + key_index) % len(Vigenere.ALPHABET)]
          else:
            new_char = Vigenere.ALPHABET[(char_index - key_index) % len(Vigenere.ALPHABET)]
        crypted_message += new_char
        
        if self._debug:
          old_char = chalk.blue(char + " (" + str(char_index) + ")")
          key_char = chalk.cyan.dim("\t with key: " + key[i % len(key)] + " (" + str(key_index) + ")")
          new_char = chalk.green("\tresult: " + new_char)
          print(chalk.yellow("DEBUG: ") + old_char + key_char + new_char)
        
        i += 1
        
      result.append(crypted_message)
      crypted_message = str()
    return " ".join(result)
