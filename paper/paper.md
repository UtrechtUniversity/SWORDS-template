---
title: "SWORDS: A framework for the Scan and revieW of Open Research Data and Software"
tags:
  - Python
  - data analysis
  - FAIR
  - open science
authors:
  - name: Keven Quach
    orcid: 0009-0002-7017-0331
    equal-contrib: true
    corresponding: true 
    affiliation: 1
  - name: Jonathan de Bruin
    orcid: 0000-0002-4297-0502
    equal-contrib: true
    affiliation: 2
  - name: Anna-Lena Lamprecht
    orcid: 0000-0003-1953-5606
    equal-contrib: true
    affiliation: 3
affiliations:
 - name: Independent Researcher, Germany
   index: 1
 - name: Utrecht University, Netherlands
   index: 2
 - name: University of Potsdam, Germany
   index: 3
date: 18 June 2023
bibliography: paper.bib

---

# Summary

SWORDS (Scan and revieW of Open Research Data and Software) is a framework designed to provide insights into an organization's open-source activities through a structured approach. The framework is divided into three core stages that can be executed independently:

1. Finding GitHub user profiles associated with an organization.  
   ![Phase 1](../docs/Phase_1.png){width=50%}
2. Extracting relevant repositories.  
   ![Phase 1](../docs/Phase_2.png){width=50%}
3. Studying the contents of the repositories. Content evaluation includes aspects of quality assessment, documentation availability, and FAIRness [@wilkinson_fair_2016] scores [@Spaaks_howfairis_2022] (Findability, Accessibility, Interoperability, and Reusability).  
   ![Phase 1](../docs/Phase_3.png){width=50%}

Written in Python, SWORDS provides a template for easy implementation within any organization and focuses on GitHub, which is the go-to reference for mining open-source repositories [@cosentino_systematic_2017]. The framework was applied to Utrecht University as part of a research project [@quach_mapping_2022]. The results of the aforementioned research project were presented at a conference [@quach_keven_2023_8150215]. Ongoing research projects are currently being conducted at the University of Potsdam.

# Statement of need

Open Science, promoting transparency in academic publications, data, software, and other types of output, is crucial for enhancing scientific and societal impact in today's research climate. The application of Open Science principles to research data and software is vital for ensuring scientific integrity and reproducibility, which can sometimes be lackluster [@allison:2016]. However, substantial challenges persist in tracking, managing, and understanding open-source research software due to the scattered and fragmented nature of these activities across multiple platforms [@lamprecht_towards_2020].

The SWORDS framework addresses this need by providing a systematic approach to collating, analyzing, and understanding an organization's open-source research software. The insights gained from implementing SWORDS can help organizations connect initiatives, improve quality, reward and recognize contributions, and foster a collaborative and open research environment. Thus, SWORDS presents an invaluable tool for any research organization aiming to improve and better understand its open-source activities and drive forward Open Science.


# Acknowledgements

We acknowledge contributions from Christopher Slewe during the genesis of this project.

# References
