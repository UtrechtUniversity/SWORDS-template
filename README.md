# Welcome to SWORDS

Welcome to the **S**can and revie**W** of **O**pen **R**esearch **D**ata and **S**oftware (**SWORDS**) project. The SWORDS project is a powerful framework to gain insights in the open source activities of your, but not limited to, university or research institute. This repository is the start of your own implementation for your organisation! Read this part carefully. For any questions, please use the issue tracker. 

This repository contists of 2 parts, the instruction and the template. The instruction is what you are reading right now, the template starts at the `<<< The template starts here >>>` below. To implement SWORDS easily, we recommend to make use of the template function in GitHub. The instruction below helps you to implement SWORDS for your organisation step-by-step. 

## Getting started with SWORDS

1. Define a name for your project. The recommended name is SWORDS@{INSERT YOUR ORGANISATION NAME ABBRAVATION}. 
2. [Create a repository from the SWORDS template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) with the name as defined in step 1. 
3. Replace all fields in the README of your repostitory starting with `{INSERT ...}` by your details of your project and organisation. 
4. Delete in the README everything between `<!-- REMOVE EVERYTHING BEFORE THIS LINE IN STEP 4 -->`. 

## <<< The template starts here >>>
<!-- REMOVE EVERYTHING BEFORE THIS LINE IN STEP 4 -->

# SWORDS@{INSERT YOUR ORGANISATION NAME ABBRAVATION}

![banner](docs/banner.png)

This repository implements for the [**S**can and revie**W** of **O**pen **R**esearch **D**ata and **S**oftware (SWORDS)](https://github.com/UtrechtUniversity/SWORDS-template) framework. SWORDS is a powerful tool to gain insights in the open source activities of your, but not limited to, university or research institute. Studies show that open source contributions can be very benificial for organisation and society. SWORDS is devided into 3 stages that can be exectued and analyzed standalone: finding user profiles associated to your organisation, extract relevant repositories, and study the contents of the respositories. 

<p align="center">
  This repository is an implementation of SWORDS for <b>{INSERT YOUR ORGANISATION NAME}</b>.
   <!-- For example Utrecht University -->
</p>
<p align="center">
  <b>SWORDS@{INSERT YOUR ORGANISATION NAME ABBRAVATION}</b>
  <!-- For example SWORDS@UU -->
</p>

<!-- Example of logo for your organisation

<p align="center">
  <img src="https://www.uu.nl/sites/default/files/styles/image_1600xn/public/cm_hs_new_logo_2021.png">
</p>

-->


- This project is a collaboration of the Research IT and ICS Department, supported by the Open Science Platform. In order to promote open science, Utrecht University has launched the Open Science Programme. To add focus to specific topics, there are four tracks within the Programme: Open access, FAIR data and software, Public engagement, Recognition and rewards. Within the track of FAIR data and software, a research project regarding the Scan and revieW of Open Research Data and Software at Utrecht University (SWORDS@UU) has been conducted.  

- Its goal is to analyze the FAIRness of GitHub repositories of Utrecht University researchers and see how they develop and manage software. While the analysis and data collection is done for Utrecht University researchers only, the purpose of this research is to serve as a template for other researchers to scan and review repositories for their university as well.

The project is split into 3 phases that correspond to the folder structure. The following hyperlinks lead to the detailed readme of each phase.

1. [User collection](collect_users/README.md)
2. [Repository collection](collect_repositories/README.md)
3. [Variable collection](collect_variables/README.md)

Each phase consists of several Python scripts and file outputs, mainly in .csv format. There is also a corresponding interactive data analysis jupyter notebook file in each phase. You can find the whole pipeline as a diagram under [Pipeline](#flowchart).

For more information about the phases, please look into the corresponding subfolders for further information on installation and usage. Note that every .csv output has a datestamp column named **date**.

## Pipeline

<p align="center">
  <img src="SWORDS_basic_flow.drawio.png">
</p>

## Contact

For technical questions, you contact either [Keven Quach](https://github.com/kequach) or [Jonathan de Bruin](https://github.com/J535D165) or open an issue on GitHub.

## Contributors

This project was implemented by de Bruin, J., Quach, K., Slewe, C., & Lamprecht, A. (2021).

### Citation

Use this citation for citing the SWORDS implementation of Utrecht University.
```
@software{de_Bruin_Scan_and_revieW_2021,
author = {de Bruin, Jonathan and Quach, Keven and Slewe, Christopher and Lamprecht, Anna-Lena},
month = {9},
title = {{Scan and revieW of Open Research Data and Software at Utrecht University}},
url = {https://github.com/UtrechtUniversity/SWORDS-UU},
version = {1.0.0},
year = {2021}
}
```

Use this citation for citing the SWORDS template.
```
@software{de_Bruin_Scan_and_revieW_2021,
author = {de Bruin, Jonathan and Quach, Keven and Slewe, Christopher and Lamprecht, Anna-Lena},
month = {9},
title = {{Template of Scan and revieW of Open Research Data and Software}},
url = {https://github.com/UtrechtUniversity/SWORDS-template},
version = {1.0.0},
year = {2021}
}
```

## Attribution

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
