# Project-4

The data was downloaded from UCI Machine Learning Repository. This dataset is related to the white variants of the Portuguese "Vinho Verde" wine. Reference [Cortez et al., 2009] for more details. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.). This dataset can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more average wines than excellent or poor ones represented). Outlier detection algorithms was used to detect the few excellent or poor wines. Also, our analysis has shown not all input variables has an impact or were relevance.

In each dataset, there’re 12 variables: 

Acidity’s importance to wine cannot be understated, as it contributes freshness, acts as a preserving agent, and helps, notably, with microbial stability. Anna Katharine Mansfield, an associate professor of enology at [Cornell University](https://grapesandwine.cals.cornell.edu/), says, “They’re two different measures: concentration of acid (TA), versus acid strength (pH).”

1. Fixed acidity, the fixed acids involved with wine that do not evaporate readily; 

2. Volatile acidity, the amount of acetic acids in wine, which at too high of levels can lead to an unpleasant, vinegar taste; 

3. Citric acid, which is found in small quantities but can add “freshness” and flavor to wines; 

4. Residual sugar, the amount of sugar remaining after fermentation stops; 

5. Chlorides, the amount of salt in the wine; 

6. Free sulfur dioxide, the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion, which prevents microbial growth and the oxidation of wine; 

7. Total sulfur dioxide, amount of free and bound forms of SO2; 

8. Density, the density of water is close to that of water depending on the percent alcohol and sugar content; 

9. PH, describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic); winemakers will often mention their pH as an indication of character, to point out whether a particular cuvée is energetic and fresh or more smooth and ripe. Acids have a pH less than 7.0 while bases have a pH higher than 7.0. Plain water measures 7.0. Most wines fall between 3.0 and 3.6.

10. Sulphates, a wine additive which can contribute to sulfur dioxide gas (S02) levels, which acts as an antimicrobial and antioxidant; 

11. Alcohol, the percent alcohol content of the wine; and 

12. Quality, the sensory data, median of at least 3 evaluations graded by wine experts between 0 (very bad) and 10 (very excellent).