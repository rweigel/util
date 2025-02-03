def compare_dicts(obj1, obj2, restructure_str=True, indent=None, depth=0):

  def str_restructure(val):
    val = val.split("\n")
    if len(val) == 1:
      if val[0] != '__NOKEY__':
        val = f"'{val[0]}'"
      else:
        val = val[0]
    return val

  if indent is None:
    indent = '  '
  if depth == 0:
    indent0 = ''
    indent1 = indent
  else:
    indent0 = depth*indent
    indent1 = indent0 + indent

  keys_all = [*list(obj1.keys()), *list(obj2.keys())]
  keys_uniq = list(set(keys_all))

  for key in keys_uniq:
    print(f"{indent0}{key}")

    val1 = obj1.get(key, "__NOKEY__")
    val2 = obj2.get(key, "__NOKEY__")

    if isinstance(val1, dict) and isinstance(val2, dict):
      compare_dicts(val1, val2, restructure_str=restructure_str, indent=indent, depth=depth+1)
      continue

    if isinstance(val1, str) and restructure_str:
      val1 = str_restructure(val1)
    if isinstance(val2, str) and restructure_str:
      val2 = str_restructure(val2)


    print(f"{indent1}Master: {val1}")
    print(f"{indent1}File:   {val2}")
