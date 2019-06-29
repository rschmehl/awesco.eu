---
title: 'Airborne Wind Energy'
subtitle: 'An introduction to an emerging technology.'
summary: An introduction to an emerging technology.
authors:
- roland-schmehl
tags:
- Airborne Wind Energy
categories: []
date: "2019-06-20T00:00:00Z"
lastmod: "2019-06-20T00:00:00Z"
featured: true
draft: false
type: posts

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal point options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
image:
  caption: ''
  focal_point: "Center"
  preview_only: false

gallery_item:
- album: AWEC
  image: awec2010_stanford.jpg
  weight: 1
  caption: 2nd Airborne Wind Energy Conference, Stanford University, CA, USA, 2010
- album: AWEC
  image: awec2011_leuven.jpg
  weight: 2
  caption: 3rd Airborne Wind Energy Conference, Leuven, Belgium, 2011
- album: AWEC
  image: awec2013_berlin.jpg
  weight: 3
  caption: 5th Airborne Wind Energy Conference, Berlin, Germany, 2013
- album: AWEC
  image: awec2015_delft.jpg
  weight: 4
  caption: 6th Airborne Wind Energy Conference, Delft, The Netherlands, 2015
- album: AWEC
  image: awec2017_freiburg.jpg
  weight: 5
  caption: 7th Airborne Wind Energy Conference, Freiburg, Germany, 2017

- album: BoA
  image: 1-BoA-2011.jpg
  weight: 1
  caption: Book of Abstract of the Airborne Wind Energy Conference 2011 in Leuven, Belgium
- album: BoA
  image: 2-BoA-2013.jpg
  weight: 2
  caption: Book of Abstract of the Airborne Wind Energy Conference 2013 in Berlin, Germany
- album: BoA
  image: 3-BoA-2015.jpg
  weight: 3
  caption: Book of Abstract of the Airborne Wind Energy Conference 2013 in Delft, The Netherlands
- album: BoA
  image: 4-BoA-2017.jpg
  weight: 4
  caption: Book of Abstract of the Airborne Wind Energy Conference 2017 in Freiburg, Germany

- album: Makani
  image: 1-makani.jpg
  weight: 1
  caption: Transportation of Makani's 600 kW energy kite to the test location in California (28 October 2016)
- album: Makani
  image: 2-makani.jpg
  weight: 2
  caption: Flying the Makani M600 prototype in California (6 January 2015)
- album: Makani
  image: 3-makani.jpg
  weight: 3
  caption: Flying the Makani M600 prototype in California (12 April 2017)
- album: Makani
  image: 4-makani.jpg
  weight: 4
  caption: Flying the Makani M600 prototype in California (Spring 2017)
- album: Makani
  image: 5-makani.jpg
  weight: 5
  caption: Installation of a new ground station at Parker Ranch on Hawaii (2018)

- album: Ampyx
  image: 1-ampyx.jpg
  weight: 1
  caption: Ampyx AP-2 in operation
- album: Ampyx
  image: 2-ampyx.jpg
  weight: 2
  caption: Ampyx AP-2 in operation
- album: Ampyx
  image: 3-ampyx.jpg
  weight: 3
  caption: Ampyx AP-3 rendering

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
Airborne wind energy (AWE) is the conversion of wind energy into electricity using tethered flying devices. Some concepts combine onboard wind turbines with a conducting tether, while others convert the pulling power of the flying devices on the ground. Replacing the tower of conventional wind turbines by a lightweight tether substantially reduces the material consumption and allows for continuous adjustment of the harvesting altitude to the available wind resource. The decrease in installation cost and increase in capacity factor can potentially lead to a substantial reduction of the cost of wind energy. Wind at higher altitudes is also considered to be an energy resource that has not been exploited so far.

{{% toc %}}

## Historical perspective

In the 1930s, German engineer and wind energy pioneer Hermann Honnef developed concepts for gigantic wind power plants with several rotors supported by towers that were several hundred meters high.[^1]<sup>,</sup>[^2]
[^1]: Hermann Honnef: "High Wind Power Plants". NASA Technical Translation NASA TT F-15,444, April 1974. {{< pdf_button url="https://archive.org/details/nasa_techdoc_19740011596" >}}
[^2]: Erich Hau: "Wind Turbines: Fundamentals, Technologies, Application, Economics". Springer-Verlag Berlin Heidelberg, 2006. {{< doi_button doi="10.1007/3-540-29284-5" >}}
Around the same time, German engineer Aloys van Gries, who in 1921 had authored a standard textbook on aircraft structures,[^3] filed patents for using kites to deploy wind turbines at higher altitudes.[^4]<sup>,</sup>[^5]<sup>,</sup>[^6]
[^3]: Aloys van Gries: "Flugzeugstatik". Springer-Verlag Berlin Heidelberg, 1921. {{< doi_button doi="10.1007/978-3-642-50654-3" >}}
[^4]: Aloys van Gries: "Durch Drachen getragene Windkraftmaschine zur Nutzbarmachung von Höhenwinden". Patent DE656194, 1935. {{< pdf_button url="DE656194C.pdf" >}}
[^5]: Aloys van Gries: "Improvements in or relating to Wind-driven Power". Patent GB489139, 1937. {{< pdf_button url="GB489139.pdf" >}}
[^6]: Aloys van Gries: "Moteur éolien". Patent FR825476A, 1937. {{< pdf_button url="FR825476A.pdf" >}}
Van Gries essentially proposed to combine trains of large lifter kites that had been used by many observatories around the world for high altitude measurements,[^7] with the emerging wind turbine technology.
[^7]: Werner Schmidt, William Anderson: "Kites: Pioneers of Atmospheric Research". In: Uwe Ahrens, Roland Schmehl, Moritz Diehl (Eds.) "Airborne Wind Energy", Green Energy and Technology, Springer-Verlag Berlin Heidelberg, pp. 95-116, 2013. {{< doi_button doi="10.1007/978-3-642-39965-7_6" >}}{{< pdf_button url="Schmidt2013.pdf" >}}
Precisely this idea of harvesting high altitude wind was concretized half a century later, during the 1970s energy crisis, by space age pioneer Hermann Oberth, who proposed it as an alternative to fossil fuels and nuclear power.[^8]<sup>,</sup>[^9]
[^8]: Hermann Oberth: "Verbessertes Drachenkraftwerk". Patent Application DE2720339, 1977. {{< pdf_button url="DE2720339A1.pdf" >}}
[^9]: Hermann Oberth: "Das Drachenkraftwerk". Uni Verlag, Dr. Roth-Oberth, Feucht, 1984. {{< pdf_button url="Oberth1984.pdf" >}}
At the same time, the team of Bryan W. Roberts at the University of Sydney developed and tested quad-rotorcraft for harvesting high-altitude wind energy,[^10] while Miles L. Loyd, an American engineer working at Lawrence Livermore National Laboratory, laid the foundation for quantitative analysis of AWE systems.
[^10]: Bryan W. Roberts: "Quad-Rotorcraft to Harness High-Altitude Wind Energy". In: Roland Schmehl (Ed.) "Airborne Wind Energy - Advances in Technology Development and Research", Green Energy and Technology, Springer Nature Singapore, pp. 581-601, 2018. {{< doi_button doi="10.1007/978-981-10-1947-0_23" >}}{{< pdf_button url="Roberts2018.pdf" >}}
In his seminal article,[^11]<sup>,</sup>[^12] Loyd compared the pulling power of a kite that is moving only in the direction of the tether with the maximum power of a kite that is additionally flying cross wind maneuvers.
[^11]: Miles L. Loyd: "Crosswind Kite Power". Journal of Energy, Vol. 4, No. 3, pp. 106-111, 1980 {{< doi_button doi="10.2514/3.48021" >}}{{< pdf_button url="Loyd1980.pdf" >}}
[^12]: Miles L. Loyd: "Genesis of Crosswind Kite Power". Presentation at the Airborne Wind Energy Conference (AWEC) 2010, Stanford, 28-29 September 2010. {{< pdf_button url="Loyd2010.pdf" >}}
This comparison is summarized by the following diagrams showing the power harvesting factor $\zeta = P/(\Pw S)$ as a function of the tether reeling factor $f=\vt/\vw$ for different values of the lift-to-drag ratio $\CL/\CD$ of the kite.

{{< figure_gallery src="loyd_kites_tex.svg" >}}

In this nondimensional representation, $\vw$ is the wind velocity, $\vt$ the tether deployment velocity, $\Ft$ the tether force, $P=\Ft\vt$ the pulling power, $\Pw=1/2\rho \vwexp{3}$ the wind power density and $S$ the wing surface area. For simplicity the aerodynamic lift coefficient $\CL$ is set here to 1. The two diagrams show that cross wind operation of a kite greatly increases its power output and that this increase is amplified with the lift-to-drag ratio. For higher lift-to-drag ratios the increase is more than two orders of magnitude.

For the cross wind kite, Loyd computes the maximum harvesting factor as
$$\zetaopt=\frac{4}{27} \frac{\CL^3}{\CD^2}$$
which occurs at the reeling factor
$$\fopt=\frac{1}{3}.$$
Comparing the two diagrams, it is obvious that cross-wind operation drastically increases the electricity output.

Loyd also investigated onboard conversion for a kite flying cross wind at constant tether length and concluded that the performance is similar to ground-based conversion. The two different conversion modes are illustrated in the following figure, where $\vvkt$ and $\vvkr$ are the tangential and radial components of the kite velocity $\vvk$.

{{< figure_gallery src="loyd_concepts_tex.svg" >}}

Loyd predicted that a large tethered aircraft could theoretically produce from 7 up to 45 MW of electrical power, which was far beyond what wind turbines at these times could generate. On the other hand, many of the effects neglected in the idealized analysis, such as the mass of the kite and tether as well as the aerodynamic drag of the tether, would significantly reduce the available power. Also, flying systems are generally more complex than wind turbines on the ground, with more degrees of freedom, possible sources of failure and more severe consequences of failures. The automation of flight operation, particularly launching and landing, is challenging and substantial advances in material science, control technology and mechatronics would be required before practical implementations could be realized. It would in fact take another 20 to 25 years and the imminent threat of global warming to trigger a renewed interest in AWE as a source of renewable energy, eventually leading to networked R&D activities and an emerging industry.

## Development as an industry

Just before the turn of the century, TU Delft professor and former astronaut [Wubbo Ockels](https://www.esa.int/Our_Activities/Human_and_Robotic_Exploration/Astronauts/Wubbo_J._Ockels) presented a high altitude wind energy concept based on a cable loop that was running from a ground station into the sky.[^13]
[^13]: Wubbo Ockels: "Laddermill, a novel concept to exploit the energy in the airspace". Aircraft Design, Vol. 4, No. 2-3, pp. 81-97, 2001. {{< doi_button doi="10.1016/S1369-8869(01)00002-7" >}}
Driven by kites attached at regular intervals, the mechanical net traction power in the loop was to be converted into electricity at the ground. Although this “laddermill” was only a conceptual idea the persistent effort of Ockels would lead to the establishment of a [research group](http://www.kitepower.eu) in 2004, spinning off two pioneering companies, [Ampyx Power](http://www.ampyxpower.com) (2007) and [Kitepower](http://www.kitepower.nl) (2016). The increasing number of institutions involved in AWE worldwide is illustrated in the following diagram.

{{< figure_gallery src="awe-emergence.svg" >}}

Included are only those academic groups or commercial teams that have been actively involved in research and development of entire AWE systems - individual researchers or inventors, component suppliers and investors are not included. From 2008 to 2010 the community experiences a substantial growth and in 2018, the R&D landscape comprised more than 60 institutions, which is illustrated in the following map.[^14]
[^14]: Roland Schmehl: "Critical Barriers for Airborne Wind Energy Systems Development". Invited presentation at the Validation Workshop for the "Study on Challenges in the Commercialisation of Airborne Wind Energy Systems", EU Headquarters, Brussels, 4 July 2018.

{{< figure_gallery src="awe-worldmap.svg" >}}

The main contributing regions are North America and Europe, with the difference that the activities in the US are dominated by [Makani](http://www.makanipower.com), a former [Google moonshot project](https://x.company), while in Europe they are distributed to a diverse network of companies, universities and research organisations. Funding through the European Union's Framework Programmes FP7 and Horizon 2020 has played an important role in the formation of this ecosystem.

Using a lightweight tether in place of a tower and its foundation removes most of the mechanical constraints of the system. For this reason, control and optimization have already early on evolved into key research themes for AWE. In 2001, Moritz Diehl described the crosswind operation of a kite as an optimal control problem,[^15]
[^15]: Moritz Diehl: "Real-Time Optimization for Large Scale Nonlinear Processes". PhD dissertation, University of Heidelberg, 2001. {{< doi_button doi="10.11588/heidok.00001659" >}}{{< pdf_button url="https://cdn.syscop.de/publications/Diehl2001.pdf" >}}
expanding this later on the basis of a prestigious FP7 Starting Grant [HighWind](https://cordis.europa.eu/project/rcn/98087/) (2011-2017) awarded by the European Research Council (ERC). A first PhD dissertation entirely dedicated to control of AWE systems was defended in 2009 by Lorenzo Fagiano,[^16]
[^16]: Lorenzo Fagiano: "Control of Tethered Airfoils for High-Altitude Wind Energy Generation". PhD dissertation, Politecnico di Milano, 2009. {{< pdf_button url="https://re.public.polimi.it/retrieve/handle/11311/1006424/161264/PhD_thesis_Fagiano_Final.pdf" >}}
who would become the most productive author of AWE literature.[^17]
[^17]: Anny K.S. Mendonça, Caroline R. Vaz, Álvaro G.R. Lezana, Cristiane A. Anacleto, Edson P. Paladini: "Comparing Patent and Scientific Literature in Airborne Wind Energy". Sustainability Vol. 9, No. 6, Article-No. 915, 2017. {{< doi_button doi="10.3390/su9060915" >}}
With the H2020 ITN doctoral training network [AWESCO](https://cordis.europa.eu/project/rcn/193938/) (2015-2018) control and optimization was complemented by modelling and simulation. Next to these more scientifically oriented projects, the EU awarded several H2020 projects to also support the industrial development of the technology: the Fast Track to Innovation (FTI) project [REACH](https://cordis.europa.eu/project/rcn/199241/), as well as the SME Instrument projects [AMPYXAP3](https://cordis.europa.eu/project/rcn/197306/), [Nextwind](https://cordis.europa.eu/project/rcn/210686/), [Skypull](https://cordis.europa.eu/project/rcn/213639/), [EK200-AWESOME](https://cordis.europa.eu/project/rcn/205145/), [AWESOME](https://cordis.europa.eu/project/rcn/221049/) and the Eurostars project [TwingPower](https://www.eurostars-eureka.eu/project/id/11105).

The substantial growth of the R&D community in 2008 also intensified the need for an international platform to share and exchange results and results, to network and explore opportunities for collaboration. Accordingly, the first Airborne Wind Energy Conference (AWEC) was held in Chico, California, in 2009. Although this event was more a symposium than an international conference, it marked the starting point for a regular get-together of the international AWE community. The following group photos were taken at the AWEC's in Stanford (2010), Leuven (2011), [Hampton (2012)](http://www.awec2012.com/), Berlin (2013), [Delft (2015)](http://www.awec2015.com) and [Freiburg (2017)](http://www.awec207.com), with the two most recent events attracting each more than 200 participants.

{{< gallery album="AWEC" height="85px" >}}

Starting with the conference in Leuven, accepted abstracts have also been published in illustrated books of abstracts. The covers of these booklets, that are available free of charge online from the [institutional repository](https://repository.tudelft.nl/islandora/search/AWEC?f%5B0%5D=mods_genre_s%3A%22conference%22) of TU Delft, are shown in the following.


{{< gallery album="BoA" height="130px" >}}

The complete bibliographic information is listed on the [website](https://awec2019.com/book-of-abstracts-series) of the AWEC 2019, which will be held in Glasgow from 15-16 October. Presentations at the conferences in Delft and Freiburg were video-recorded and deposited online together with the posters. As a result, the two conference websites present rather complete snapshots of the technology development status in 2015 and 2017.

It was also the AWEC 2011 in Leuven, at which a petition to the European Parliament and the European Commissioners for better support of the technology was signed by 76 developers.[^18]
[^18]: Wubbo Ockels et al: Petition letter to the members of the European Parliament and the European Commissioners. Leuven, 2 December 2011. {{< pdf_button url="Petition2011.pdf" >}}
Following several years of systematic support of the technology development, the European Union commissioned a study on the challenges in the commercialization of AWE systems to a consortium lead by Dutch consultancy company [Ecorys](https://www.ecorys.com). A stakeholder workshop at the EU headquarters in Brussels was held in July 2018 and a key conclusion of the final report[^19]
[^19]: Karel van Hussen et al: "Study on Challenges in the Commercialisation of Airborne Wind Energy Systems". ECORYS Report PP-05081-2016, Brussels, September 2018. {{< doi_button doi="10.2777/87591" >}}
was that “the technology is still immature, and that it remains unclear whether the technology can ultimately reach cost-competitiveness”. As an important action the assessment team recommended to prove continuous operation of AWE systems and to deepen the insight into the resource potential and complementarity. [Airborne Wind Europe](http://www.airbornewindeurope.org/) was founded in 2018 as an association of European AWE industry and academia, with the objective to coordinate the commercial development activities and to establish joint working groups on important collaborative topics, such as safety and technical guidelines, airspace regulation, environmental impact and a sector-wide technology development roadmap. Regular meetings of the working groups have started in 2019.

It is interesting to note that AWE developed essentially in parallel to classical wind energy, with only little interaction between the two fields. While wind turbines are becoming the leading source of new renewable energy capacity in Europe, the US and Canada, with global installed power expanding from 17.4 GW in 2000 to 591 GW in 2018, the R&D activities in AWE have been carried by a vibrant startup community with many commonalities and strong ties to the unmanned aerial vehicle (UAV) sector. First collaborations started to emerge after the research group of TU Delft was integrated into the section of Wind Energy in 2014 and Fort Felker, a former director of the [National Wind Technology Center](https://www.nrel.gov/nwtc/) of NREL, started as CEO of Makani / X in 2015. The Airborne Wind Energy Conferences 2015 and 2017 have experienced increasing interest also from the wind energy community and, vice versa, also wind energy conferences are increasingly visited by the AWE community. For example, at the Wind Energy Science Conference (WESC) 2019 in Cork, at least 18 presentations were about AWE. During this conference, the European Academy of Wind Energy (EAWE) established a [Airborne Wind Energy Committee](https://eawe.eu/organisation/committees/) to represent the academic community in Europe.

## Presently pursued concepts

The presently pursued AWE technologies can be classified according to the following scheme.

{{< figure_gallery src="classification.svg" >}}

At the highest level we differentiate between electricity generation with a fixed ground station, with a moving ground station or directly on the flying device, requiring a conducting tether. Concepts using a moving ground station, such as a horizontal loop track or a carousel-type construction, are technically quite complex and still relatively far from realization. At the second level we distinguish between concepts using individual tethered devices that fly cross wind maneuvers and concepts using flying rotors. Multi-drone concepts and fully automated take-off and landing are challenging aspects of AWE.[^20]
[^20]: Watson et al: "“Future emerging technologies in the wind power sector: a European perspective". Renewable and Sustainable Energy Reviews (under review), 2019.
Most populated is the class of systems that use one or more individual wings, rigid or flexible, operated in crosswind flight maneuvers, generating electricity with a fixed ground station.

{{< figure_gallery src="pumping_cycle_tex.svg" >}}

A detailed analysis and assessment of the different concepts has been presented by Cherubini et al.[^21]
[^21]: Antonello Cherubini, Andrea Papini, Rocco Vertechy, Marco Fontana: "Airborne Wind Energy Systems: A review of the technologies". Renewable and Sustainable Energy Reviews, Vol. 51, pp. 1461-1476, 2015. {{< doi_button doi="doi:10.1016/j.rser.2015.07.053" >}}

The largest prototype in operation is the M600 developed by Makani. It uses 8 wind turbines onboard the wing of 28 m span. More details can be found on the websites of Makani and X. Makani has already early sought the approval of the FAA, publishing a response.

{{< gallery album="Makani" height="85px" >}}

Ampyx

{{< gallery album="Ampyx" height="85px" >}}

Kitepower

{{< gallery album="Kitepower" height="85px" >}}

Others: Windswept, Kitemill, Twingtec, Enerkite

{{< gallery album="Others" height="85px" >}}
