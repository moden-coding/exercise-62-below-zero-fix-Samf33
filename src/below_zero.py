#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv", index_col=0)
    return len(df[df["Air temperature (degC)"] < 0])
def main():
    result = below_zero()
    print(f"Number of days below zero: {result}")
if __name__ == "__main__":
    main()
