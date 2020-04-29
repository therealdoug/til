# Format String of JSON to pretty print
Sometimes when working with JSON you'll get an unformatted blob file.  Using
python, vim can reformat that for you

`:%!python -m json.tool`
