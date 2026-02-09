import pytest
from pytest_mock import mocker
from src.data_loader.file_checker import (
    NSWClimateDataPortal,
    check_filename,
    check_file_ensembles,
)


nsw = NSWClimateDataPortal()


@pytest.mark.parametrize(
    "filename, varname, ensemble_attributes, expected",
    [
        (
            "tasmaxAdjust_ssp126_ACCESS-ESM1-5_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
            "tasmax",
            nsw,
            True,
        ),
        (
            "tasmaxAdjust_ssp126_ACCESS-ESM1-5_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
            "tasmin",
            nsw,
            False,
        ),
        ("tasmax_ACCESS-ESM1-5", "tasmax", nsw, False),
        ("tasmax_NARCliM2-0-WRF412R3", "tasmax", nsw, False),
    ],
)
def test_check_filename(filename, varname, ensemble_attributes, expected):
    assert (
        check_filename(
            filename=filename, variable=varname, ensemble_attributes=ensemble_attributes
        )
        == expected
    )


_MOCK_FILES: list[str] = [
    "tasmaxAdjust_ssp245_ACCESS-ESM1-5_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_ACCESS-ESM1-5_NARCliM2-0-WRF412R5_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_EC-Earth3-Veg_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_EC-Earth3-Veg_NARCliM2-0-WRF412R5_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_MPI-ESM1-2-HR_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_MPI-ESM1-2-HR_NARCliM2-0-WRF412R5_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_NorESM2-MM_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_NorESM2-MM_NARCliM2-0-WRF412R5_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_UKESM1-0-LL_NARCliM2-0-WRF412R3_NARCliM2-0-SEAus-04i.nc",
    "tasmaxAdjust_ssp245_UKESM1-0-LL_NARCliM2-0-WRF412R5_NARCliM2-0-SEAus-04i.nc",
]


@pytest.mark.parametrize(
    "filenames, varname, ensemble_attributes, extension, expected",
    [
        (_MOCK_FILES, "tasmax", nsw, "nc", True),
        (_MOCK_FILES, "tasmin", nsw, "nc", False),
        (_MOCK_FILES, "tasmax", nsw, "tif", False),
        (_MOCK_FILES[:-1], "tasmax", nsw, "nc", False),
    ],
    ids=["full_ensemble", "wrong_var", "wrong_ext", "incomplete_list"],
)
def test_check_file_ensembles(
    mocker, filenames, varname, ensemble_attributes, extension, expected
):

    # mock os.listdir inside check_file_ensembles
    mocker.patch(
        "src.data_loader.file_checker.os.listdir",
        return_value=filenames,
    )
    assert (
        check_file_ensembles(
            path="",  # leave path empty since underlying os.listdir mocker is present
            variable=varname,
            ensemble_attributes=ensemble_attributes,
            extension=extension,
        )
        == expected
    )
