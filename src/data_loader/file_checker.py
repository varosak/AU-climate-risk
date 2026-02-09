from abc import ABC, abstractmethod
import os
from src.data_loader.dataset_attributes.nsw_climate_data_portal import (
    RCM_NAMES,
    GCM_NAMES,
    EXPECTED_MODEL_AMOUNT,
)


class EnsembleAttributes(ABC):
    @property
    @abstractmethod
    def rcm(self) -> list[str]: ...
    @property
    @abstractmethod
    def gcm(self) -> list[str]: ...
    @property
    @abstractmethod
    def expected_ensemble_amount(self) -> int: ...


class NSWClimateDataPortal(EnsembleAttributes):
    rcm: list[str] = RCM_NAMES
    gcm: list[str] = GCM_NAMES
    expected_ensemble_amount: int = EXPECTED_MODEL_AMOUNT


def check_filename(
    filename: str, variable: str, ensemble_attributes: EnsembleAttributes
) -> bool:
    """
    Check if a file name has the specified GCM, RCM, and variable name
    Returns boolean
    """
    if not variable.lower() in filename.lower():
        return False
    if not any(model.lower() in filename.lower() for model in ensemble_attributes.rcm):
        return False
    if not any(model.lower() in filename.lower() for model in ensemble_attributes.gcm):
        return False
    return True


def check_file_ensembles(
    path: str,
    variable: str,
    ensemble_attributes: EnsembleAttributes,
    extension: str = "nc",
) -> bool:
    """
    Check file ensembles in a specified path/folder have all the required ensembles
    """
    folder_files: list[str] = os.listdir(path=path)
    # filter out files that do not contain the parameters in file name
    valid_files: list[str] = [
        file
        for file in folder_files
        if file.endswith(extension)  # extension check
        and check_filename(
            filename=file, variable=variable, ensemble_attributes=ensemble_attributes
        )  # climate model-related checks
    ]
    # check complete ensembles
    if len(valid_files) != ensemble_attributes.expected_ensemble_amount:
        return False
    return True
