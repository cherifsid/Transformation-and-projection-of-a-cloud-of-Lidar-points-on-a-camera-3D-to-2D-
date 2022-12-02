# Transformation-and-projection-of-a-cloud-of-Lidar-points-on-a-camera-3D-to-2D-
Transformation and projection of a cloud of Lidar points on a camera (3D to 2D)

In this part we will use the transformations provided by the Kitti dataset : https://www.cvlibs.net/datasets/kitti/ to project a 3D point cloud (Source Lidar/Velodyne) on the image plane of the first color camera(left).
<p>
  <img src="/result/KITTI_ENVIREMNT.PNG" width="1000" />
</p>

This is not just allow to know the depth of a set of 2d points in the image, but also to know the color of the 3D points. We can then <a href="https://github.com/cherifsid/Transformation-and-projection-of-a-cloud-of-Lidar-points-on-a-camera-3D-to-2D-">(Project source)</a> build a cloud of colored points.

The objective of this practical work is to carry out the example in Result figure figure .
The plotted points represent the projection of 3D points in the image. The color of each dot indicates the depth of this point.
The 'jet' color map is used in this case

Result : 

<p>
  <img src="/result/plot.png" width="1000" />
</p>
