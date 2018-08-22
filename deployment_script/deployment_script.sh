#!/bin/bash

virtualenv flash
 git clone https://github.com/nagaraju0wifi/messagepoint_test.git
 cd messagepoint_test
 pip install pathlib
 pip install pymysql
 pip install json
 pip install shutil
 pip install string
 pip install random

 python app_with_*.py

