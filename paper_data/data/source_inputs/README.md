# Supporting inputs and upstream notices

This directory contains the small inputs distributed with the GitHub notebook
companion. They are not part of the Zenodo data archives. Any license selected
for this repository applies only to Charlie Phillips's copyrightable
contributions to the extent permitted; upstream materials retain their own
terms and attribution requirements.

## U.S. Energy Information Administration

The EIA-860 workbooks and EIA-930-derived actual-load and renewable-generation
files originate with the U.S. Energy Information Administration. EIA states
that its U.S. government publications and data are public domain and may be used
or distributed, while recommending an acknowledgment that identifies EIA and
the publication date. See the official
[EIA Copyrights and Reuse policy](https://www.eia.gov/about/copyrights_reuse.php).

Suggested acknowledgment: "Source: U.S. Energy Information Administration,
EIA-860 and EIA-930 data, accessed for this study."

## NREL and U.S. Department of Energy data

The weather-grid mappings, modeled capacity-factor validation series, and SAM
configuration inputs use NREL data or software. NREL's official data notice
grants users the right to use or copy the data without charge provided that the
notice is retained, requires credit to DOE/NREL/Alliance in resulting
publications, disclaims warranties, and prohibits implying endorsement. The
data are provided as-is. Retain this notice and consult the complete official
[NREL Disclaimer and Data and Software terms](https://www.nrel.gov/disclaimer.html)
when copying or redistributing these materials.

Suggested acknowledgment: "This work used data and software made available by
the U.S. Department of Energy's National Renewable Energy Laboratory, operated
by the Alliance for Sustainable Energy, LLC."

## U.S. Census Bureau

The population, FIPS, and county-point provenance files are derived from public
2020 Census redistricting and TIGER/Line products. Census Bureau employee-created
data and works generally are not subject to U.S. copyright protection, although
third-party content may have separate terms. See the Census Bureau's
[research transparency policy](https://www.census.gov/topics/research/research-transparency-public-access/policy.html)
and [policies and notices](https://www.census.gov/about/policies.html). Cite the
specific Census products and vintages listed in
[`paper_data/SOURCES.md`](../../SOURCES.md).

## GCAM-USA

The eight annual state electricity-demand scenario files are GCAM-USA model
outputs used to scale state load. Credit the Joint Global Change Research
Institute and cite the GCAM-USA documentation. GCAM documentation is distributed
under the Educational Community License 2.0; retain applicable license and
attribution notices when redistributing GCAM materials. See the
[GCAM documentation repository](https://github.com/JGCRI/gcam-doc) and
[GCAM-USA documentation](https://github.com/JGCRI/gcam-doc/blob/gh-pages/gcam-usa.md).

## No credentials

This directory must never contain API keys, HSDS credentials, access tokens, or
local configuration files. Store credentials only in an ignored `.env` file or
another untracked local credential store.
