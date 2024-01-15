import platform
import os

print("platform: ", platform.system())
print("printing env vars:")
for key, value in sorted(os.environ.items()):
    print("    ", key, value)
