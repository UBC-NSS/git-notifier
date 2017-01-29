import cgi
import re

# pylint: disable=bad-indentation

# separates the commit message, diff, and tags
_separator = '>' + ('-'*63) + '\n'

# separates multiple emails in a changeset
_emailsep = '>' + ('*'*63)

_pattern = re.compile('(  +)')

def _mangle_line(line):
  content = cgi.escape(line)
  m = _pattern.finditer(content)
  for i in reversed(list(m)):
    (start, end) = i.span()
    content = content[:start] + ('&nbsp;' * (end-start)) + content[end:]

  if content.startswith('-'):
    return '<tt style="color:#800">%s</tt>' % (content)
  if content.startswith('+'):
    return '<tt style="color:#080">%s</tt>' % (content)
  return content

def _breakemail(text):
  def _convert_block(text):
    return [_mangle_line(l) for l in text.splitlines()]

  output = []
  for i, blk in enumerate(text.split(_separator)):
    if i > 0:
      output.append('<hr>')
    output.extend(_convert_block(blk))
  return "<br>".join(output)

def _breakbody(text):
  return ("<hr style='" +
          "height: 3px; background-color: #eee; border: solid 1px; color: #ccc;'" +
          "></hr>").join(
              [_breakemail(emailtext) for emailtext in text.split(_emailsep)])

def htmlify(text):
  return ('<html><body><tt>' +
          _breakbody(text) +
          '</tt></body></html>')
