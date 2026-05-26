from geospatial_data_science_toolkit import GeospatialData, DataCube, GeoAI
import time


def main():
    ti = time.time()
    
    variables_list = [
                        "HH",
                        "HV",
                        "VV",
                        "VH",
                    ]
    collection_name = "COPERNICUS/S1_GRD"
    
    roi = [-8.389435, 32.784965, -7.975388, 33.015573]
    data_lake_folder = r"data\sentinel1_africa_2020"
    
    
    gdst = GeospatialData()
    
    gdst.download_bands_gee_chunked(
        collection_name=collection_name,
        bands_list=variables_list,
        start_date="2020-01-01",
        end_date="2020-12-31",
        roi=roi,
        scale=10,
        output_folder=data_lake_folder,
    )
    
    print(time.time() - ti)
    

if __name__ == '__main__':
    main()
