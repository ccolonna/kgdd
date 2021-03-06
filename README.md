# KGDD 

KG Test Driven Design development. Write queries with expected results. CONSTRUCT KG. Run tests and see if queries return correct bindings.

![screen-gif](./assets/example.gif)

## Run tests

To run a testbed on a KG run:

`kgdd -f "/path/to/KG.{ttl,nt,...}" -t "/path/to/tests.json"`

## Testbed 

To create a testbed write a `.json` file like the following:

```json
{
    "tests" : [
        {
            "description" : "Extract all the triples from a KG",
            "query" : "SELECT * WHERE {?s ?p ?o } ",
            "results" : 3,
            "rows": [{
                "s" : "artist_1"
            }            ],

            "bindings": {
                "o" : "music_1"
            },
            "skip": false
        }
        ...
    ]
}
```

Every item in the `tests` array will be used to run a test. Let's see fields:

- `query`: The query to be run to extract data from KG.
- `results`: The number of expected rows. With 0 or a value greater than 0 then the test will pass if the numbers match. With -1 the  test will pass if you get a number greater than 0.
- `rows`: Every item in the array is an expected row. For the test to pass you need at least a row matching all the expected ones. In this example we want at least a row with `"artist_1"` as `"s"`.
- `bindings`: At least a binding in at least a results row for all the specified variable in the bindings object should match for the test to pass. In this example At least in a `"o"` in one of the row should match `"music_1"`.
- `skip`: The test will be skipped.

In every field you can set `null` as default value if you don't want the results, rows, or bindings step to run.
E.g. following testbed will run only results step.

```json
{
    "tests" : [
        {
            "description" : "Extract all the triples from a KG",
            "query" : "SELECT * WHERE {?s ?p ?o } ",
            "results" : 3,
            "rows": null,
            "bindings": null,
            "skip": false
        }
        ...
    ]
}
```

## Usage

```
usage: kgdd [-h] -t TEST -f FILE [-v {0,1,2}]

A cli program to automate TDD KG development. Define some basic query and expected outputs in a test. Kgdd will take
care of run queries and see if they match expedted results.

options:
  -h, --help            show this help message and exit
  -t TEST, --test TEST  Path to testbed file. File should be in Json format
  -f FILE, --file FILE  Path to KG file
  -v {0,1,2}, --verbose {0,1,2}
                        Verbose output. Verbosity level = 0,1,2 . Default 0 no verbose. 2 is really verbose
```

## Installation

`kgdd` is a python package to install it you need python `3.X` installed. You can install it globally in your local machine running:

```
pip install kgdd
```

or on Windows:

```
py -m pip install kgdd
```

Alternatively if you prefere a local installation you can create a virtualenv and install the package there.
The package is distributed as a cli tool, and available everywhere if the environment where is installed is activated. 