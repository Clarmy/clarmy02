from clarmy02 import trans_coord


def test_trans_coord():
    xs, ys = trans_coord(116.407718, 39.912721)

    assert (12958447.89, 4853267.23) == (round(xs, 2), round(ys, 2))
