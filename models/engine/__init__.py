"""
this package imports file_storage and creates an instance of FileStorage
"""

import models.engine.file_storage
storage = models.engine.file_storage.FileStorage()
storage.reload()
print("INIT", storage.all())
