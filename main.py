import logging
import os
import comp630

with open("jmr1178.moto", "rb") as f:
    object_name = os.path.basename(f.name)
    exception_or_True = comp630.to_the_cloud(f.name, "comp630-m1-f22", f"jmr1178/{object_name}")
    print(f"Upload Successful: {exception_or_True}")
