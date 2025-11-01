def avg_rainfall_last_n_years(rainfall_df, state, n):
    last_year = rainfall_df['Year'].max()
    start = last_year - n + 1
    df = rainfall_df[(rainfall_df['State']==state) & (rainfall_df['Year']>=start)]
    if df.empty:
        return None
    return df['Rainfall_mm'].mean()

def top_m_crops(crops_df, state, n, m):
    last_year = crops_df['Year'].max()
    start = last_year - n + 1
    df = crops_df[(crops_df['State']==state) & (crops_df['Year']>=start)]
    agg = df.groupby('Crop')['Production_tonnes'].sum().reset_index()
    agg = agg.sort_values('Production_tonnes', ascending=False)
    return agg.head(m)
