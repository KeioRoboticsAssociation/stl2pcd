import open3d as o3d

def main():
    # 1. STLファイルの読み込み
    mesh = o3d.io.read_triangle_mesh("/home/osw/Downloads/field_NHK2026.stl")

    # 2. メッシュ表面から点をサンプリング
    # number_of_points: 生成する点の数
    # init_factor: サンプリングの初期密度（ポアソンディスクサンプリング用）
    pcd = mesh.sample_points_poisson_disk(number_of_points=500000)

    # (オプション) 点群の可視化
    # o3d.visualization.draw_geometries([pcd])

    # 3. PCDファイルとして保存
    o3d.io.write_point_cloud("output.pcd", pcd)


if __name__ == "__main__":
    main()
