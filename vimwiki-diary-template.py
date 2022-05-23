#!/usr/bin/env python3

import sys
import datetime
from pathlib import Path


try:
    date = Path(sys.argv[1]).stem
except:
    date = datetime.date.today()

body = f"""# {date}: 



## tasks | due:{date} or scheduled:{date} or +OVERDUE
"""

print(body)
