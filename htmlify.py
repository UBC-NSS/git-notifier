import re

_pattern = re.compile('(  +)')

def _mangle_line(line):
  content = line
  m = _pattern.finditer(content)
  for i in reversed(list(m)):
    (start, end) = i.span()
    content = content[:start] + ('&nbsp;' * (end-start)) + content[end:]

  if content.startswith('-'):
    return '<tt style="color:#800">%s</tt>' % (content)
  if content.startswith('+'):
    return '<tt style="color:#080">%s</tt>' % (content)
  return content

def htmlify(text):
  lines = text.splitlines()
  lines = [_mangle_line(l) for l in lines]

  return '<html><body><tt>%s</tt></body></html>' % "<br>".join(lines)
