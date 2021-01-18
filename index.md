FunPDBe Data Exchange Format (JSON Schema)
=====
[![Build Status](https://travis-ci.com/PDBe-KB/funpdbe-schema.svg?branch=master)](https://travis-ci.com/PDBe-KB/funpdbe-schema)
[![codecov](https://codecov.io/gh/PDBe-KB/funpdbe-schema/branch/master/graph/badge.svg?token=EOQT5D0I49)](https://codecov.io/gh/PDBe-KB/funpdbe-schema)
[![Maintainability](https://api.codeclimate.com/v1/badges/9da3c56481123d4f9225/maintainability)](https://codeclimate.com/github/PDBe-KB/funpdbe-schema/maintainability)

This is the repository of the FunPDBe JSON Schema

Quick start
-----------

There are two main files:

* funpdbe_schema.json
* funpdbe_example.json

There is also a very basic JSON validator that shows how to validate a JSON file against the schema:

```
# install dependencies
pip install -r requirements.txt

# run the validator
cd basic_validator
python3 basic_validator/basic_validator.py path/to/schema.json path/to/json/file.json
```

This will run a simple validation, using the jsonschema package. It will use the schema from the path "path/to/schema.json" and validate the json at the path "path/to/example.json" against it.

Schema
------

The JSON schema specifies all the details of the data exhange format that is used by FunPDBe. For more information on how JSON schemas work, please refer to http://json-schema.org/

Example
-------

The file funpdbe_example.json is an example of a JSON file with data in a format that is acceptable by the FunPDBe deposition system.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags.

## Authors

* **Mihaly Varadi** - *Initial work* - [mvaradi](https://gitlab.ebi.ac.uk/mvaradi)

## License

This project is licensed under the EMBL-EBI License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

We would like to thank the PDBe team for their support and feedback, as well as all the members of the FunPDBe consortium:

* PDBe team - [team website](https://www.ebi.ac.uk/services/teams/pdbe)
* Orengo team - [CATH](http://www.cathdb.info/)
* Vranken team - [DynaMine](http://dynamine.ibsquare.be/)
* Barton team - [NoD](http://www.compbio.dundee.ac.uk/www-nod/)
* Wass team - [3DLigandSite](http://www.sbg.bio.ic.ac.uk/3dligandsite/)
* Blundell team - [CREDO](http://marid.bioc.cam.ac.uk/credo)
* Fraternali team - [POPSCOMP](https://mathbio.crick.ac.uk/wiki/POPSCOMP)
