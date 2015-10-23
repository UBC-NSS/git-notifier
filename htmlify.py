def _mangle_line(line):
  content = line.lstrip()
  leadingspaces = '&nbsp;' * (len(line)-len(content))

  if content.startswith('-'):
    return '<span style="color:#800">%s%s</span>' % (leadingspaces, content)
  if content.startswith('+'):
    return '<span style="color:#080">%s%s</span>' % (leadingspaces, content)
  return '%s%s' % (leadingspaces, content)


def htmlify(text):
  lines = text.splitlines()
  lines = [_mangle_line(l) for l in lines]

  return '<html><body><tt>%s</tt></body></html>' % "<br>".join(lines)
