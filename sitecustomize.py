import os
import sys

root = os.path.dirname(os.path.abspath(__file__))

# Prevent the project root from shadowing stdlib modules such as logging.
# The current working directory entry ("") is often inserted first, which causes
# imports like import logging to resolve to the local project package instead of
# the real stdlib module.
for entry in ["", root]:
    if entry in sys.path:
        sys.path.remove(entry)

# Re-add the project root after the stdlib paths so local application modules
# remain importable without taking precedence over stdlib modules.
sys.path.append(root)

# Ensure Python's stdlib package resolution is not polluted by the local
# project package named 'logging'.
if os.path.isdir(os.path.join(root, "logging")):
    sys.modules.pop("logging", None)
