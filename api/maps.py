from leafmap import leafmap
#url = 'https://open.gishub.org/data/landsat/timeseries.zip'
#leafmap.download_file(url)

m = leafmap.Map()
m.add_stac_layer(
    collection="landsat-c2-l2",
    item="LC09_L2SP_047026_20220305_02_T1",
    assets="red",
    rescale="0,12000",
    colormap_name="reds",
)

outfp = "/home/m/spacex/map.html"

m.save(outfp)