#!/usr/bin/python

def boxplot_sorted(df, by, column, rot=0):
    # use dict comprehension to create new dataframe from the iterable groupby object
    # each group name becomes a column in the new dataframe
    df2 = pd.DataFrame({col:vals[column] for col, vals in df.groupby(by)})
    # find and sort the median values in this new dataframe
    meds = df2.median().sort_values()
    # use the columns in the dataframe, ordered sorted by median value
    # return axes so changes can be made outside the function
    boxprops = dict(linewidth=2)
    return df2[meds.index].boxplot(rot=rot, return_type="axes", figsize=(20,10), boxprops=boxprops)

def dataDescribe(df):
    
    df_mean = df.groupby(df.index).mean()
    df_median = df.groupby(df.index).median()
    df_std = df.groupby(df.index).std()
    df_sum = df.groupby(df.index).sum()
    
    months = df.index.unique()
    
    df_desc = pd.DataFrame(columns=['Month','Mean','Median','Std Dev','Variance','Skewness','Kurtosis','Min','Max','Sum'])
    for m in months:
        d = describe(df.loc[df.index==m], axis=0)
        median = df_median[df_total_median.index==m].bytes[0]
        std = df_std[df_total_sd.index==m].bytes[0]
        total = df_sum[df_total_sum.index==m].bytes[0] 
        df_desc = df_desc.append({'Month':m,
                                            'Mean':d.mean[0],
                                            'Median': median,
                                            'Std Dev':std,
                                            'Variance': d.variance[0],
                                            'Skewness': d.skewness[0],
                                            'Kurtosis': d.kurtosis[0],
                                            'Min': d.minmax[0][0],
                                            'Max': d.minmax[1][0],
                                            'Sum': total
                                           } , ignore_index=True)

    return df_desc