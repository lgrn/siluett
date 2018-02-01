# siluett

This python script takes an `input.txt` text file with NPL-ID:s and queries the "Sil Online" API for the associated market name, and prints them. For more info: https://silonline.silinfo.se

## Getting Started

You need a Python interpreter and an input file with values. 

## Example usage

I have included an example `input.txt` containing the following two values:

```
20100709000050
19880617000116
```

If you simply run the script, this will be the output:

```
NPLID;Handelsnamn;
20100709000050;Alvedon Novum;
19880617000116;Alvedon® forte;
```

Most likely, you want this output to a file:

`> python .\siluett.py > output.csv`

## Contributing

All suggestions, improvements or patches are welcome.

## License

This project is in the public domain - see the [LICENSE](LICENSE) file for details.
