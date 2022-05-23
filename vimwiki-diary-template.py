#!/usr/bin/env python3

import sys
import datetime


date = sys.argv[1].rsplit(".", 1)[0] if len(sys.argv) > 1 else datetime.date.today()

body = f"""# {date}: 



## tasks | due:{date} or scheduled:{date} or +OVERDUE
"""

print(body)
