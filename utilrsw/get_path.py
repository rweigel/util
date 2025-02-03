def get_path(obj, path):
  if isinstance(path, str):
    if '.' in path:
      path = path.split('.')
    else:
      path = [path]

  for key in path:
    if obj is None:
      return None
    if key not in obj:
      return None
    obj = obj[key]

  return obj
