require "html/table"
include HTML

table = HTML::Table.new{ |t|
  t.border  = 1
  t.bgcolor = "red"
}

table.push Table::Row.new{ |r|
  r.align   = "left"
  r.bgcolor = "green"
  r.content = ["foo","bar","baz"]
}

row = Table::Row.new{ |r|
  r.align   = "right"
  r.bgcolor = "blue"
  r.content = "hello world"
}

table[1] = row

puts table.html

#### output ####
<table border=1 bgcolor='red'>
  <tr align='left' bgcolor='green'>  # row 0
     <td>foo</td>                    # column 0
     <td>bar</td>                    # column 1
     <td>baz</td>                    # column 2
  </tr>
  <tr align='right' bgcolor='blue'>  # row 1
     <td>hello world</td>            # column 0
  </tr>
</table>
