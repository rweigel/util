import collections

def sort_dict(d):
  if not isinstance(d, dict):
    return d
  d = collections.OrderedDict(sorted(d.items()))
  for key in d:
    d[key] = sort_dict(d[key])
  return d
