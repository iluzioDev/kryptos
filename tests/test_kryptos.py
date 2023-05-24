
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 2023

@author: iluzioDev
@project: kryptos
@file: test_kryptos.py

@description: Test file for kryptos library
"""
import unittest
from kryptos.modules.vigenere import Vigenere

class TestVigenereEncryption(unittest.TestCase):
  def test_1(self):
    self.assertEqual(Vigenere.encrypt("hello", "key"), "RIJVS")
  def test_2(self):
    self.assertEqual(Vigenere.encrypt("Godskin Apostle", "Maliketh"), "SOOAUMG HBODBVI")
  def test_3(self):
    self.assertEqual(Vigenere.encrypt("Ganon", "Link"), "RIAYY")

class TestVigenereDecryption(unittest.TestCase):
  def test_1(self):
    self.assertEqual(Vigenere.decrypt("RIJVS", "key"), "HELLO")
  def test_2(self):
    self.assertEqual(Vigenere.decrypt("SOOAUMG HBODBVI", "Maliketh"), "GODSKIN APOSTLE")
  def test_3(self):
    self.assertEqual(Vigenere.decrypt("RIAYY", "Link"), "GANON")

if __name__ == '__main__':
    unittest.main()
