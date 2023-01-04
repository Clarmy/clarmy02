import pyproj


def trans_coord(lon, lat):
    prj = pyproj.Transformer.from_crs(crs_from=4326, crs_to=3857, always_xy=True)
    xs, ys = prj.transform(lon, lat)

    return xs, ys


if __name__ == "__main__":
    print(trans_coord(116.407718, 39.912721))  # 北京坐标
