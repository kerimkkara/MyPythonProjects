# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:30:27 2023

@author: bhblack
"""

from pytube import YouTube

url = input("Url giriniz: ");

yt = YouTube(url)
# En yüksek kalitede videoyu indirin
stream = yt.streams.get_highest_resolution()
stream.download()