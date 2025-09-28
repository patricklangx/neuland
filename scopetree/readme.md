# scopetree

Script to generate a vertical tree structure of scope exported from burp suite. Helps to visualize the scope.

## Usage

```bash
python3 scopetree.py -file <scope input file> -height 1000 -width 1000
```

Define the `-height` and `-width` based on the depth of nodes. The larger the scope, the larger the height and width should be, e.g., an input file with 1000 urls should have a height and width of at least 10000.
