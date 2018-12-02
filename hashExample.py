import hashlib
print hashlib.new("md5","HELLO").hexdigest()
print hashlib.new("md5","HELLOa").hexdigest()
print hashlib.new("sha1","HELLO").hexdigest()
print hashlib.new("sha256","HELLO").hexdigest()