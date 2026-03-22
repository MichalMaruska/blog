---
title: "Gitk on wide displays"
date: 2026-02-12
draft: false
---

# Gitk on wide displays

## Gitk on wide displays

This is the original layout of gitk:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSdMYSar7F7or4reqsmk4MEXMBNNWXerArOf_da0_bJ2t-UStRktdOGOj-Y4BAStDxqFoRfhTkYsPqsA5L9HnJCLTdJyWagjl2ECyc5LFPFiZ8Avegqcdl4E1qQVdfBksmBN0O_nZ8MzPMDntRM8USWStK0r6ICBHvtU-tqg-CfJWwHndHeUnkC79NYKE/w585-h414/gitk-vertical.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSdMYSar7F7or4reqsmk4MEXMBNNWXerArOf_da0_bJ2t-UStRktdOGOj-Y4BAStDxqFoRfhTkYsPqsA5L9HnJCLTdJyWagjl2ECyc5LFPFiZ8Avegqcdl4E1qQVdfBksmBN0O_nZ8MzPMDntRM8USWStK0r6ICBHvtU-tqg-CfJWwHndHeUnkC79NYKE/s2955/gitk-vertical.png)

  
 I realized (years ago) that competing for height, while there is abundant space to the sides  is bad.

It's better to keep "lists" to the side, while the main **diff pane** should use the full height.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiU9VatsEnCuoY2sfarQ8QhjvLZMI1gdtdaUztruOnGTdAKlfdlfug6ZTW4cbZNuFNijaQgkLm2plK-4X1iDWW1BHyQzwpUav8ITZN_TO0XujQkbKiGvwWF_OuAAug4GdVrzs4Iji35M123VJ_2FrEwB6LXWCr-wBk-F37QPWMNgbARpd8hR9rMrAhKss8/w596-h339/gitk-wide.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiU9VatsEnCuoY2sfarQ8QhjvLZMI1gdtdaUztruOnGTdAKlfdlfug6ZTW4cbZNuFNijaQgkLm2plK-4X1iDWW1BHyQzwpUav8ITZN_TO0XujQkbKiGvwWF_OuAAug4GdVrzs4Iji35M123VJ_2FrEwB6LXWCr-wBk-F37QPWMNgbARpd8hR9rMrAhKss8/s3408/gitk-wide.png)

  
 the changes are in [gitk-wide branch](https://github.com/MichalMaruska/git/commits/gitk-wide/)
