"""Autograding script."""

import os

import pandas as pd  # type: ignore
from homework.word_count import run_job


def test_01():
    """Test word count job."""

    run_job("input/", "output")

    #
    # Retorna error si el archivo "_SUCCESS" no existe en la
    # carpeta output/
    if not os.path.exists("output/_SUCCESS"):
        raise FileNotFoundError("File 'output/_SUCCESS' not found")

    #
    # Retorna error si la carpeta output/ no existe
    if not os.path.exists("output/part-00000"):
        raise FileNotFoundError("File 'output/part-00000' not found")

    #
    # Lee el contenido del archivo output.txt
    dataframe = pd.read_csv(
        "output/part-00000",
        delimiter="\t",
        header=None,
        names=["word", "count"],
    )
    dataframe = dataframe.set_index("word")
    series = dataframe["count"]

    assert series["analytics"] == 5
    assert series["business"] == 7
    assert series["by"] == 3
    assert series["algorithms"] == 2
    assert series["analysis"] == 4
