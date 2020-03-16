Changelog
==========

* 25/04/2018 - "evidence_code_ontology" is required
* 25/04/2018 - "evidence_code_ontology" has to be minimum 1 element long list
* 25/04/2018 - "evidence_code_ontology.eco_code" is required
* 25/04/2018 - "evidence_code_ontology.eco_code" has pattern "^ECO_[0-9]{7}$"
* 25/04/2018 - "sites.site_id" is required
* 25/04/2018 - "sites.source_release_date" has pattern "^[0-3][0-9]/[0-1][0-9]/[1-2][0-9]{3}$"
* 25/04/2018 - "release_date" has pattern "^[0-3][0-9]/[0-1][0-9]/[1-2][0-9]{3}$"
* 25/04/2018 - "pdb_id" has pattern "^[0-9][a-z][a-z0-9]{2}$"
* 25/04/2018 - "chains.residues.aa_type" has pattern "^[A-Z]{3}$"
* 25/04/2018 - "chains.residues.site_data.raw_score is required
* 25/04/2018 - "chains.residues.site_data.confidence_score is required
* 25/04/2018 - "chains.residues.site_data.confidence_classification is required
* 25/04/2018 - "chains.residues.site_data.confidence_classification is enum of ["high", "medium", "low", "null"]
* 10/05/2018 - "release_date" has pattern "^[0-3]*[0-9]/[0-1]*[0-9]/[1-2][0-9]{3}$"
* 10/05/2018 - "sites.source_release_date" has pattern "^[0-3]*[0-9]/[0-1]*[0-9]/[1-2][0-9]{3}$"
* 15/05/2018 - "additional_site_annotations" added to "sites"
* 04/06/2018 - "sites" is required (site_data was already referencing it)
* 06/06/2018 - "pdb_id" has pattern "^[1-9][a-zA-Z0-9]{3}$"
* 18/06/2018 - "chains.residues.aa_type" has pattern "^[A-Za-z0-9]+$"
* 19/07/2018 - "source_database" is optional
* 19/07/2018 - "source_accession" is optional
* 24/10/2018 - "confidence_score" can be greater than 1.0, if the calculation method justifies it
* 15/01/2019 - "confidence_score" is optional - curated annotations don't have confidence score
* 15/01/2019 - "raw_score" is optional - curated annotations don't have raw scores
* 15/01/2019 - "curated" added to "confidence_classification" enumeration list
* 15/01/2019 - allow additional annotations fields
* 22/03/2019 - "aa_variant" is an optional field in "site_data" for mutations/variants
* 10/09/2019 - "site_url" is an optional field in "sites" for linking directly to site information
* 16/09/2019 - "source_version" is an optional field for the version of data which was used to derive annotations
* 02/03/2020 - "model_coordinates_url" is an optional URL field for providing structural models which the annotations are based on
* 02/03/2020 - "includes_het_groups" is an optional boolean (true/false) field to indicate if the entry contains annotations for HET groups
* 16/03/2020 - "aa_variant_causes" is an optional string field for recording the specific effect of a variant