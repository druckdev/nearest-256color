# nearest-256color
Finds the closest color available with a 256 color terminal.
Uses [data.json](data.json) taken from [jonasjacek/colors](https://github.com/jonasjacek/colors/blob/3cc893056c7d9d945f5dcc24553122c003159cf9/data.json)

## Example usage
```sh
$ ./find_nearest_color.py "#AD7FA8"
{'colorId': 139, 'hexString': '#af87af', 'rgb': {'r': 175, 'g': 135, 'b': 175}, 'hsl': {'h': 300, 's': 20, 'l': 60}, 'name': 'Grey63'}

$ ./find_nearest_color.py "fce94f"
{'colorId': 221, 'hexString': '#ffd75f', 'rgb': {'r': 255, 'g': 215, 'b': 95}, 'hsl': {'h': 45, 's': 100, 'l': 68}, 'name': 'LightGoldenrod2'}
```
