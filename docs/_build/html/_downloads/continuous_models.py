"""
Basic Usage
===========

This tutorial illustrates how to estimate a simple model with one continuous predictor. We're going to fit a model with random intercepts, slopes and their correlations. 95% confidence intevals will be estimated using the Wald-method assuming a quadratic likelihood surface.

"""
##########################################
# Import module and check out data
# --------------------------------
#

import os
import pandas as pd
import seaborn as sns
from pymer4.models import Lmer
from pymer4.utils import get_resource_path

df = pd.read_csv(os.path.join(get_resource_path(),'sample_data.csv'))
df.head()

#######################################################################
# Estimate a model
# ----------------
#
# Initialize linear model with random intercepts, slopes and their correlation

model = Lmer('DV ~ IV2 + (IV2|Subject)',data=df)

#########################################################################
# Fit it

model.fit()

#######################################################################
# Inspect clusters
# --------------------------
#
# We can look at the 'Subject' level parameters easily
# Each row here is a unique Subject's random intercept and slope

model.fixef.head()

# We can also plot these values with respect to the population parameters

model.plot('IV2',plot_ci=True)


########################################################################
# Inspect Fit
# -----------
#
# We can make a quick residual plot to assess our fit
# pymer conveniently saves residuals within an internal copy of the inputted dataframe

sns.regplot(x= 'IV2',
            y= 'residuals',
            data= model.data,
            fit_reg= False
            )

#######################################################################
# We can similarly compare predicted values (fits) to true values to see how well this model captures the data, using seaborn to compute within group boot-strapped confidence intervals

sns.regplot(x= 'fits',
            y= 'DV',
            units= 'Group',
            data= model.data,
            fit_reg= True
            )
