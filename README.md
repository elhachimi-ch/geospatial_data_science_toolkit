# Geospatial Data Science Toolkit

A practical Python toolkit for geospatial data acquisition, data cube processing, and geospatial AI workflows.

This project provides utilities to:
- Download remote sensing and climate datasets (Google Earth Engine, Sentinel Hub, AWS, and related backends).
- Build geospatial time series and region-based data products.
- Work with Zarr data cubes and export/visualize raster outputs.
- Train and run AI models for geospatial tasks through a unified `GeoAI` interface.

## Table of Contents
- [Geospatial Data Science Toolkit](#geospatial-data-science-toolkit)
  - [Table of Contents](#table-of-contents)
  - [Key Functionalities](#key-functionalities)
    - [1) GeospatialData](#1-geospatialdata)
    - [2) DataCube](#2-datacube)
    - [3) GeoAI](#3-geoai)
  - [Library Structure](#library-structure)
  - [Installation](#installation)
    - [Option A: Clone the repository](#option-a-clone-the-repository)
    - [Option B: Create and activate a virtual environment (recommended)](#option-b-create-and-activate-a-virtual-environment-recommended)
    - [Install core dependencies](#install-core-dependencies)
  - [Quick Start](#quick-start)
  - [Example Workflow](#example-workflow)
  - [Requirements](#requirements)
  - [Citation](#citation)

## Key Functionalities

### 1) GeospatialData
Main entry point for geospatial data operations.

Common capabilities include:
- Band/time-series downloads from Earth observation collections.
- Region-of-interest raster extraction.
- Chunked downloading for large spatiotemporal requests.
- Point-based and ROI-based time-series generation.
- Raster visualization and helper utilities.

### 2) DataCube
High-level interface for working with spatiotemporal data cubes.

Includes:
- Loading Zarr datasets.
- Visualizing variables for specific timestamps.
- Exporting selected variables and dates to GeoTIFF.

### 3) GeoAI
AI layer for model training/inference on geospatial data.

Supports:
- Multiple model backends (for example: tabformer, xgboost, catboost, random_forest, tabpfn).
- CPU/GPU device setup.
- Model save/load and structure inspection.

## Library Structure
- `geospatial_data_science_toolkit.py`: Core classes and methods (`GeospatialData`, `DataCube`, `GeoAI`, and supporting data loaders).
- `kitchen_gdst.py`: Example script showing how to download Sentinel-1 bands in a chunked workflow.

## Installation

### Option A: Clone the repository
```bash
git clone https://github.com/elhachimi-ch/geospatial_data_science_toolkit.git
cd geospatial_data_science_toolkit
```

### Option B: Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
```

Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### Install core dependencies
```bash
pip install numpy pandas matplotlib scikit-learn geopandas rasterio fiona shapely xarray rioxarray dask pyarrow tqdm torch earthengine-api geemap sentinelhub
```

Note:
- You may need additional packages depending on your workflow and optional backends.
- Some methods require configured credentials (for example Google Earth Engine and Sentinel Hub).

## Quick Start

```python
from geospatial_data_science_toolkit import GeospatialData

gdst = GeospatialData()

gdst.download_bands_gee_chunked(
    collection_name="COPERNICUS/S1_GRD",
    bands_list=["HH", "HV", "VV", "VH"],
    start_date="2020-01-01",
    end_date="2020-12-31",
    roi=[-8.389435, 32.784965, -7.975388, 33.015573],
    scale=10,
    output_folder="data/sentinel1_africa_2020",
)
```

## Example Workflow
1. Initialize `GeospatialData` for data acquisition.
2. Download or extract imagery/time-series for your ROI.
3. Build or load a Zarr cube with `DataCube`.
4. Visualize and export features as GeoTIFF.
5. Train or run models with `GeoAI`.

## Requirements
- Python 3.10+ recommended.
- Adequate memory/storage for raster-heavy workloads.
- Access credentials for selected cloud data sources.

## Citation
If you use this toolkit in academic work, please cite it as:

```bibtex

Will be updated with more specific citation information as the project evolves.

```
