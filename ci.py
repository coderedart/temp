import platform
import os

print("platform: ", platform.system())
print("printing env vars:")
for key, value in os.environ.items():
    print("    ", key, value)
