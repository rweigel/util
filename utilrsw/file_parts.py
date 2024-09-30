import os

def file_parts(full_path):
  drive, dir = os.path.splitdrive(full_path)
  dir, file  = os.path.split(dir)
  ext = ""
  fname_split = os.path.splitext(os.path.basename(file))
  if len(fname_split) > 1:
    file_root, ext = fname_split
    if ext.startswith('.'):
      ext = ext[1:]
  return {'drive': drive, 'dir': dir, 'file': file + ext, 'root': file_root, 'ext': ext}

if __name__ == "__main__":
  print(file_parts('c:/dir1/dir2/file.ext'))