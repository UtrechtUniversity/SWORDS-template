---
title: "SWORDS: A framework for the Scan and revieW of Open Research Data and Software"
tags:
  - Python
  - data analysis
  - FAIR
  - open science
authors:
  - name: Jonathan de Bruin
    orcid: 0000-0002-4297-0502
    equal-contrib: true
    affiliation: 1
  - name: Keven Quach
    orcid: 0009-0002-7017-0331
    equal-contrib: true
    affiliation: 3
  - name: Anna-Lena Lamprecht
    orcid: 0000-0003-1953-5606
    equal-contrib: true
    corresponding: true # (Who should be the corresponding author in our case?)
    affiliation: 2
affiliations:
 - name: Utrecht University, Netherlands
   index: 1
 - name: University of Potsdam, Germany
   index: 2
 - name: Independent Researcher, Germany
   index: 3
date: 18 June 2023
bibliography: paper.bib

---

# Summary

SWORDS (Scan and revieW of Open Research Data and Software) project is an open-source framework designed to provide insight into an organization's open-source activities. This comprehensive tool offers a structured approach for organizations such as universities and research institutes to evaluate their contributions to the open-source community. The framework is divided into three core stages that can be executed independently:

1. Finding user profiles associated with an organization.  
   ![Phase 1](../docs/Phase_1.png){width=50%}
2. Extracting relevant repositories.  
   ![Phase 1](../docs/Phase_2.png){width=50%}
3. Studying the contents of the repositories. Content evaluation includes aspects of quality assessment, documentation availability, and FAIRness [@wilkinson_fair_2016] scores [@Spaaks_howfairis] (Findability, Accessibility, Interoperability, and Reusability).  
   ![Phase 1](../docs/Phase_3.png){width=50%}

Written in Python, the SWORDS project provides a template for easy implementation within any organization and focuses on GitHub, which is the go-to reference for mining open-source repositories [@cosentino_systematic_2017]

# Statement of need

Open Science, promoting transparency in academic publications, data, software, and other types of output, is crucial for enhancing scientific and societal impact in today's research climate. The application of Open Science principles to research data and software is vital for ensuring scientific integrity and reproducibility, which can sometimes be lackluster [@allison:2016]. However, substantial challenges persist in tracking, managing, and understanding open-source research software due to the scattered and fragmented nature of these activities across multiple platforms [@lamprecht_towards_2020].

The SWORDS framework addresses this need by providing a systematic approach to collating, analyzing, and understanding an organization's open-source research software. The insights gained from implementing SWORDS can help organizations connect initiatives, improve quality, reward and recognize contributions, and foster a collaborative and open research environment. Thus, SWORDS presents an invaluable tool for any research organization aiming to improve its open-source activities and drive forward the principles of Open Science.


# Acknowledgements

<!-- Either use acknowledgement or add Chris as an author -->
We acknowledge contributions from Christopher Slewe during the genesis of this project.

# References