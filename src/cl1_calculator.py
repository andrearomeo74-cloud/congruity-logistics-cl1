import pandas as pd

EPSILON = 1e-9

def calculate_cl(df):
    """
    Calculate Congruity Logistics (CL) metric.

    CL = V / (E + I + S + epsilon)

    V = useful logistics value
    E = energy dissipation
    I = informational dissipation
    S = structural dissipation
    """

    # V: useful logistics value
    V = (df["payload"] * df["useful_km"]).sum()

    # E: energy dissipation
    E = df["fuel"].sum()

    # I: informational dissipation
    I = (
        df["replans"].sum()
        + df["exceptions"].sum()
        + df["delay"].sum()
        + df["rework"].sum()
    )

    # S: structural dissipation
    S = (
        df["empty_km"].sum()
        + df["idle_time"].sum()
    )

    CL = V / (E + I + S + EPSILON)

    return CL


def calculate_cl_components(df):
    """
    Return individual components for inspection.
    """

    V = (df["payload"] * df["useful_km"]).sum()

    E = df["fuel"].sum()

    I = (
        df["replans"].sum()
        + df["exceptions"].sum()
        + df["delay"].sum()
        + df["rework"].sum()
    )

    S = (
        df["empty_km"].sum()
        + df["idle_time"].sum()
    )

    CL = V / (E + I + S + EPSILON)

    return {
        "V": V,
        "E": E,
        "I": I,
        "S": S,
        "CL": CL
    }
