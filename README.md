# gsimcli:
Geostatistical SIMulation for the homogenisation and interpolation of
CLImate data

## What is it

**gsimcli** is a proposed method to homogenise climate data using
geostatistical stochastic simulation methods.

It is presented here as a *work in progress* Python project. Some of its
modules are intended to serve as useful libraries for other projects.

## Development

In a first stage, **gsimcli** will be implemented using **Direct Sequential
Simulation** (DSS) [1]. The method description and its application have already
been published [2].

It is planned to develop an implementation using Direct Sequential Simulation
with **local distributions**.

This research project is hosted at [ISEGI-NOVA](http://www.isegi.unl.pt)
(Lisbon, Portugal) and it is funded by the "Fundação para a Ciência e
Tecnologia" ([FCT](http://www.fct.pt)), Portugal, through the research project
PTDC/GEO-MET/4026/2012. See [approval and funding notice]
(http://www.isegi.unl.pt/documentos/P_GSIMCLI_EN.pdf).

![ISEGI-NOVA](/images/logo_ISEGI.png) ![FCT](/images/logo_FCT.png)

## Documentation

The documentation is hosted at readthedocs.org:
http://gsimcli.readthedocs.org

Browse and post issues and contributions [here]
(https://github.com/iled/gsimcli/issues).

## Dependencies

- [Python](http://www.python.org): 2.7
- [NumPy](http://www.numpy.org): 1.8 or higher
- [pandas](http://pandas.pydata.org) 0.13.0 or higher
- [DSS](https://sites.google.com/site/cmrpsoftware/geoms) only the binary
- [Wine](http://www.winehq.org) only for *nix systems

## License

GPLv3

## References

[1]: Soares, Amílcar. *Direct Sequential Simulation and Cosimulation.*
Mathematical Geology 33, no. 8 (2001): 911-926.
http://link.springer.com/article/10.1023/A:1012246006212.

[2]: Costa, AC, and A Soares. *Homogenization of Climate Data: Review and New
Perspectives Using Geostatistics.* Mathematical Geosciences 41, no. 3 (November
28, 2009): 291-305. doi:10.1007/s11004-008-9203-3.


## Project Publications

### Scientific Journals

Ribeiro, S., Caineta, J., Costa, A. C., Henriques, R., Soares, A. (2016) [Detection of inhomogeneities in precipitation time series in Portugal using direct sequential simulation](http://doi.org/10.1016/j.atmosres.2015.11.014). Atmospheric Research 171, 147–158. doi: 10.1016/j.atmosres.2015.11.014

Ribeiro, S., Caineta, J., Costa, A. C., (2015) [Review and discussion of homogenisation methods for climate data. Physics and Chemistry of the Earth](http://doi.org/10.1016/j.pce.2015.08.007). In press. doi: 10.1016/j.pce.2015.08.007

### Proceedings

Ribeiro, S., Caineta, J., Costa, A. C., Soares, A. (2015). [Establishment of detection and correction parameters for a geostatistical homogenisation approach](http://doi.org/10.1016/j.proenv.2015.07.115). Procedia Environmental Sciences, 27, 83-88. doi: 10.1016/j.proenv.2015.07.115

Caineta, J., Ribeiro, S., Soares, A., Costa, A. C. (2015). [Workflow for the homogenisation of climate data using geostatistical simulation](http://sgem.org/sgemlib/spip.php?article5707). In: Conference Proceedings of the 15th SGEM GeoConference on Informatics, Geoinformatics and Remote Sensing. Albena, Bulgaria, 16-25 June 2015, Vol. 1, pp. 921-929.

Ribeiro, S., Caineta, J., Costa, A. C., Henriques, R. (2015). [Analysing the detection and correction parameters in the homogenisation of climate data series using gsimcli](https://agile-online.org/Conference_Paper/cds/agile_2015/shortpapers/59/59_Paper_in_PDF.pdf ). In: F. Bacao, M. Y. Santos, M. Painho (Eds.), The 18th AGILE International Conference on Geographic Information Science, Lisbon, Portugal, 9-12 June 2015.

Caineta, J., Ribeiro, S., Henriques, R., Costa, A. C. (2015). [A Package for the homogenisation of climate data using geostatistical simulation](https://www.thinkmind.org/index.php?view=article&articleid=geoprocessing_2015_6_40_30130). In: GEOProcessing 2015: The Seventh International Conference on Advanced Geographic Information Systems, Applications, and Services, Lisbon, Portugal, 22-27 February 2015.

### Other Publications

Caineta, J., Ribeiro, S., Henriques, R., Soares, A., Costa, A. C. (2014). [Benchmarking a geostatistical procedure for the homogenisation of annual precipitation series](http://meetingorganizer.copernicus.org/EGU2014/EGU2014-7605.pdf). In: Geophysical Research Abstracts, Vol. 16, EGU2014-7605, European Geosciences Union General Assembly 2014. (Vienna, Austria, 27 April –2 May 2014)

Caineta, J., Ribeiro, S., Costa, A. C., Henriques, R., Soares, A. (2014). [Inhomogeneities detection in annual precipitation time series in Portugal using direct sequential simulation](http://meetingorganizer.copernicus.org/EGU2014/EGU2014-7849.pdf). In: Geophysical Research Abstracts, Vol. 16, EGU2014-7849, European Geosciences Union General Assembly 2014. (Vienna, Austria, 27 April –2 May 2014)

Ribeiro, S., Caineta, J., Henriques, R., Soares, A., Costa, A. C. (2014). [Advantages and applicability of commonly used homogenisation methods for climate data](http://meetingorganizer.copernicus.org/EGU2014/EGU2014-7725.pdf). In: Geophysical Research Abstracts, Vol. 16, EGU2014-7725, European Geosciences Union General Assembly 2014. (Vienna, Austria, 27 April –2 May 2014)
