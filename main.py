import open3d as o3d

def main():
    # 1. STLファイルの読み込み
    mesh = o3d.io.read_triangle_mesh("./nhk_dan_200.STL")

    # 2. メッシュ表面から点をサンプリング
    # number_of_points: 生成する点の数
    # init_factor: サンプリングの初期密度（ポアソンディスクサンプリング用）
    pcd = mesh.sample_points_poisson_disk(number_of_points=50000)

    # (オプション) 点群の可視化
    # o3d.visualization.draw_geometries([pcd])

    # 3. PCDファイルとして保存
    o3d.io.write_point_cloud("/home/osw/ilias2026_r2_ws/src/odom/ransac_manual_matching/config/dan200.pcd", pcd)


if __name__ == "__main__":
    main()
