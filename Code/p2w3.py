import os
import sys
from Crypto.Hash import SHA256

import hashlib

block_size = 1024

file1 = "6 - 1 - Introduction (11 min).mp4"
file2 = "6 - 2 - Generic birthday attack (16 min).mp4"



file_size = os.path.getsize(file1) 
last_block_size = file_size % block_size
i = 0

print file_size
with open(file1, "rb") as f:
   if last_block_size != 0:
	   m = hashlib.sha256()
	   pos = file_size - last_block_size
	   f.seek(pos,0)
	   m.update(f.read(last_block_size))
	   oldh = m.digest()
	   print pos
   
   while pos>0:
	   m = hashlib.sha256()
	   pos = pos - block_size
	   print pos
	   f.seek(pos,0)
	   chunk = f.read(1024) + oldh
	   m.update(chunk)
	   oldh = m.digest()
		   
	   
print m  
print oldh.encode('hex')

