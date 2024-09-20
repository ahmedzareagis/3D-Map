import plotly.graph_objects as go
import numpy as np

lats = np.linspace(-3.3, -2.8, 200)
lons = np.linspace(37.0, 37.6, 200) 

lons, lats = np.meshgrid(lons, lats)


elevation = np.exp(-((lats + 3.0674)**2 + (lons - 37.3556)**2) * 100) * 5895

fig = go.Figure(go.Surface(
    z=elevation,
    x=lons,  
    y=lats,
    colorscale='Viridis',
    colorbar=dict(title="Elevation (meter)", thickness=15, len=0.5),
    showscale=True,
))

fig.update_layout(
    title="3D map of Mount Kilimanjaro",
    scene=dict(
        xaxis_title='Longitude',
        yaxis_title='Latitude',
        zaxis_title='Elevation (meter)',
        aspectratio=dict(x=2, y=1, z=0.5),
        camera_eye=dict(x=1.5, y=1.5, z=0.5),
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

fig.write_html('arab_capitals_weather_map_3d.html')

print("Interactive map with current weather data has been saved to arab_capitals_weather_map_3d.html")