![Static Badge](https://img.shields.io/badge/ubuntu-18.04%7C20.04%7C22.04-brightgreen)
![Static Badge](https://img.shields.io/badge/python-3.9|3.10-007fff)
![Static Badge](https://img.shields.io/badge/license-mit-fuchsia)


# g2o Graph Optimization Lib for Ubuntu Linux

g2o with pybind is quite OS and Python version specific. For now, directly building on the system seems a straight forward way.

## Intellisense Enhanced


![sample1](https://raw.githubusercontent.com/ubicoders/g2opy/main/pics/intel0.png)


![sample2](https://raw.githubusercontent.com/ubicoders/g2opy/main/pics/intel1.png)

## Assumptions
1. Ubuntu Linux
2. In Docker environment

## Tested
- Ubuntu 18.04, 20.04, 22.04
- Python 3.9, 3.10

## Ready2Go Docker images
No extra installation reuqired for g2opy.

https://hub.docker.com/repository/docker/ubicoders/g2opy/general
```
docker pull ubicoders/g2opy:u22_p310
```
```
docker pull ubicoders/g2opy:ros2_humble
```

### Sample docker compose

```
version: "3.8"

services:
  g2o_ros2_humble:
    container_name: ros2_g2opy_cnt
    image: ubicoders/g2opy:ros2_humble
    network_mode: host
    privileged: true
    stdin_open: true
    tty: true
    environment:
      - DISPLAY
      - QT_X11_NO_MITSHM=1 
    volumes:
      - "/tmp/.X11-unix/:/tmp/.X11-unix/:rw"
      - "$HOME/.Xauthority:/root/.Xauthority:rw"
      - "/dev/:/dev/"


```

## To custom install as pip package 

```
git clone https://github.com/ubicoders/g2opy && cd g2opy
bash install.bash
```

Ideally, the above command should do all installation end-to-end. After this, g2opy package should exist in pip list.

![sample3](https://raw.githubusercontent.com/ubicoders/g2opy/main/pics/g2opy_pip.png)


## License
This g2opy module is built based on
1. https://github.com/uoip/g2opy
2. https://github.com/RainerKuemmerle/g2o
3. Eigen https://eigen.tuxfamily.org/index.php?title=Main_Page

MIT license. Currently, additional work is the build configuration on top of uoip/g2opy.

## Examples

```
python tester.py
```

```python
import numpy as np
import g2opy as g2o
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
from collections import defaultdict

def showCameraPoses(optim, idx, N):
    for i in range(idx, idx + N):
        T = optim.vertex(i).estimate().matrix()
        trans = T[:3, 3]
        print('camera pose at ', i, ': ', trans)

def calcSSE(optim, idx, wPts):
    sse = 0
    N = wPts.shape[0]
    for i in range(idx, idx + N):
        guessedWpt = optim.vertex(i)
        error = guessedWpt.estimate() - wPts[i-idx]
        sse += np.sum(error ** 2)
    return sse

def showWpts(optim, idx, N):
    for i in range(idx, idx + N):
        T = optim.vertex(i).estimate()
        #T = np.round(T, 0)
        print('guessed wPt at ', i-idx, ': ', T)

def main():
    optimizer = g2o.SparseOptimizer()
    solver = g2o.BlockSolverSE3(g2o.LinearSolverCSparseSE3())
    solver = g2o.OptimizationAlgorithmLevenberg(solver)
    optimizer.set_algorithm(solver)

    f, p = 200, 256
    baseline = 0.3
    K = np.array([[f, 0, p],
                  [0, f, p],
                  [0, 0, 1]])

    wPts = np.array([
        [0, 0, 10],
        [-1, 3, 30],
        [2, 2, 37.2],
    ])

    num_pose = 10
    for i in range(0, int(num_pose/2)):
        pose = g2o.Isometry3d(np.identity(3), [(i-2)*10, 0, 0])
        v_se3 = g2o.VertexSCam()
        v_se3.set_cam(f, f, p, p, baseline)
        v_se3.set_id(i)
        v_se3.set_estimate(pose)
        if i < 2:
            v_se3.set_fixed(True)
        v_se3.set_all() # sets transfrom, projection, dR (angle)
        optimizer.add_vertex(v_se3)

    for i in range(int(num_pose/2), num_pose):
        pose = g2o.Isometry3d(np.identity(3), [0, (i - int(num_pose/2)- 2) * 10, 0])
        v_se3 = g2o.VertexSCam()
        v_se3.set_cam(f, f, p, p, baseline)
        v_se3.set_id(i)
        v_se3.set_estimate(pose)
        v_se3.set_fixed(False)
        v_se3.set_all() # sets transfrom, projection, dR (angle)
        optimizer.add_vertex(v_se3)

    point_id = 0

    for i, wpt in enumerate(wPts):
        guessed_wPt = g2o.VertexSBAPointXYZ()
        guessed_wPt.set_id(num_pose + point_id)
        guessed_wPt.set_marginalized(True)
        guessed_wPt.set_estimate(wpt + np.random.randn(3) )
        optimizer.add_vertex(guessed_wPt)

        for j in range(num_pose):
            z = optimizer.vertex(j).map_point(wpt)
            if i > 1:
                z +=  np.random.randn(3)
            edge = g2o.Edge_XYZ_VSC()
            edge.set_vertex(0, guessed_wPt)
            edge.set_vertex(1, optimizer.vertex(j))
            edge.set_measurement(z)
            edge.set_information(np.identity(3))
            optimizer.add_edge(edge)

        point_id += 1

    sse0 = calcSSE(optimizer, num_pose, wPts)
    print('\nRMSE (inliers only):')
    print('before optimization:', np.sqrt(sse0 / wPts.shape[0]))
    showCameraPoses(optimizer, 0, num_pose)
    showWpts(optimizer, num_pose, 3)


    print('Performing full BA:')
    optimizer.initialize_optimization()
    optimizer.set_verbose(False)
    optimizer.optimize(100)

    sse1 = calcSSE(optimizer, num_pose, wPts)

    print('\nRMSE (inliers only):')
    print('after  optimization:', np.sqrt(sse1 / wPts.shape[0]))
    showCameraPoses(optimizer, 0, num_pose)
    showWpts(optimizer, num_pose, 3)


if __name__ == '__main__':
    main()
```


## Other ReadMEs from Forked and Referred Repos

- [readme-uoip/g2opy](./referred_readme_contents.md)