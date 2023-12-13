from enum import Enum
from typing import Dict, List, Union

import pandas
import pandas as pd
import pickle
import numpy as np
from sklearn import svm, datasets, ensemble, neighbors
from sklearn.svm import LinearSVC, SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import joblib
import xgboost as xgb


model_path_dict = {
    "male_che_model": "./male/male_che_gi_vote.joblib",
    "male_wai_model": "./male/male_wai_gi_vote.joblib",
    "male_hip_model": "./male/male_hip_gi_vote.joblib",
    "male_thi_model": "./male/male_thi_gi_vote.joblib",
    "male_ank_model": "./male/male_ank_gi_vote.joblib",
    "male_arm_model": "./male/male_arm_ln_vote.joblib",
    "male_osm_model": "./male/male_out_sm_vote.joblib",
    "female_che_model": "./female/female_che_gi_vote.joblib",
    "female_wai_model": "./female/female_wai_gi_gbr.joblib",
    "female_hip_model": "./female/female_hip_gi_lin.joblib",
    "female_thi_model": "./female/female_thi_gi_lin.joblib",
    "female_ank_model": "./female/female_ank_gi_lin.joblib",
    "female_arm_model": "./female/female_arm_ln_vote.joblib",
    "female_osm_model": "./female/female_out_sm_vote.joblib",
}


class GenderKey(Enum):
    MALE = "male"
    FEMALE = "female"


class BodyPartKey(Enum):
    chest = "che_model"
    waist = "wai_model"
    hip = "hip_model"
    thigh = "thi_model"
    ankle = "ank_model"
    arm = "arm_model"
    outseam = "osm_model"


def process_model_key(gender: str, body_part: str) -> str:
    return "_".join([gender, BodyPartKey[body_part]])

class User:
    def __init__(self, _gender: str, _height: float, _weight: float):
        self._gender = _gender
        self._height = _height
        self._weight = _weight
        # self.scaler = female_scaler if _gender == "female" else male_scaler
        self.training_features = ['wgt', "hgt", "wgt_log", "hgt_log", "wgt_sqr", "hgt_sqr"]

    @property
    def gender(self) -> str:
        return self._gender

    @property
    def height(self) -> float:
        return self._height

    @property
    def weight(self) -> float:
        return self._weight


    def get_df(self) -> pandas.DataFrame:
        user_data = np.array([[self.weight, self.height,
                                np.log(self.weight), np.log(self.height),
                                self.weight * self.weight, self.height * self.height]])
        user_df = pd.DataFrame(user_data, columns=self.training_features)
        male_scaler_path = "./male/male_data_scaler.pkl"
        female_scaler_path = "./female/female_data_scaler.pkl"

        if self.gender == "male":
            with open(male_scaler_path, 'rb') as f:
                scaler = pickle.load(f)
        else:
            with open(female_scaler_path, 'rb') as f:
                scaler = pickle.load(f)

        user_scaled = scaler.transform(user_df)
        return user_scaled

    def __str__(self):
        return f"{self.gender}, height: {self.height}, weight: {self.weight}"

class SizePredictor:
    def __init__(self, model_path_dict: Dict[str, Union[str]]):
        self.model_path_dict = model_path_dict

    def load_model(self, body_part: str, gender: str):
        model_name = process_model_key(gender, body_part)

        path_to_model = self.model_path_dict[model_name]
        try:
            model = joblib.load(path_to_model)
            return model
        except FileNotFoundError:
            raise(f"Model not found. Make sure the file '{path_to_model}' exists.")

    def predict(self, body_part: str, gender: str, user: User):
        # Get selected model
        model = self.load_model(body_part=body_part, gender=gender)
        features = user.get_df()

        # Perform prediction using the model
        try:
            prediction = model.predict(features)
            return prediction
        except Exception as e:
            raise(f"Error during prediction: {e}")
            return None

