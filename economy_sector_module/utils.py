from model_utils import Choices

STANDARDS = Choices(
    (0, "unspecified", "Unspecified"),
    (1, "nace", "NACE"),
    (2, "ateco", "ATECO"),
    (3, "gics", "GICS"),
    (4, "isic", "ISIC"),  # rev4
    (5, "naics", "NAICS"),  # 17 Todo-Ask Marco which one we going to use!
    (6, "sic", "SIC"),  # Todo-fill the data
    (7, "sae", "SAE"),  # Todo-fill the data
)
