Install TA commands
==========================

Python 3.12 is still new, and ta-lib may not support it fully. Try using Python 3.10 or 3.11:
-------------------------------------------------------------------
sudo apt install python3.11 python3.11-venv python3.11-dev
python3.10 -m venv venv
source venv/bin/activate
pip install ta-lib
-------------------------------------------------------------------
