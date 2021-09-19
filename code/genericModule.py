def hello():
  print('module running')

# Run when : python <file.py>
# Don't run during import
print('__name__ = ' + __name__)
if __name__ == "__main__":
  hello()
else:
  print('non uguale')