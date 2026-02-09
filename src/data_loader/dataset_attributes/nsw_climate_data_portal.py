FREQUENCIES: list[str] = [
    "daily",
    "monthly",
]  # temporal frequencies of the downloaded raster files

GCM_NAMES: list[str] = [
    "ACCESS-ESM1-5",
    "EC-Earth3-Veg",
    "MPI-ESM1-2-HR",
    "NorESM2-MM",
    "UKESM1-0-LL",
]

RCM_NAMES: list[str] = ["NARCliM2-0-WRF412R5", "NARCliM2-0-WRF412R3"]

VARIABLES: list[str] = ["tasmax", "tasmin"]

SCENARIOS: list[str] = ["Historical", "SSP126", "SSP245", "SSP370"]

EXPECTED_MODEL_AMOUNT: int = (
    10  # This is the amount of expected models in a complete ensemble from NSW Climate Data Portal for a given variable
)
