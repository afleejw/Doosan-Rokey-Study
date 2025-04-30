import rclpy  # Import the ROS 2 Python client library
from rclpy.node import Node  # Import the Node class from ROS 2
from sensor_msgs.msg import Imu  # Import the Image message type from sensor_msgs
from builtin_interfaces.msg import Time
from geometry_msgs.msg import Vector3, Quaternion

import requests
# import json

import argparse  # Import argparse for command-line arguments

class IMUNode(Node):
    def __init__(self, ip):
        super().__init__('ip_IMU_node')  # Initialize the Node with the name 'ip_stream_node'
        
        # Create a publisher for the Image topic without QoS profile
        self.publisher_ = self.create_publisher(Imu, 'ip_imu', 1)
        
        # Create a timer to call timer_callback every 0.001 seconds (approximately 100 FPS)
        self.timer = self.create_timer(0.001, self.timer_callback)
        
        self.url = f'http://{ip}/sensors.json'


    def timer_callback(self):
        try:
            # json_data = requests.get(self.url).json
            # self.data = json.loads(json_data)
            response = requests.get(self.url)
            data = response.json()

            msg = Imu()
            msg.header.stamp = Time()
            msg.header.stamp = self.get_clock().now().to_msg()
            # msg.header.stamp = accel_data = data['accel']['data'][-1][0]

            # 가속도 데이터
            accel_data = data['accel']['data'][-1][1]
            msg.linear_acceleration = Vector3(
                x=accel_data[0],
                y=accel_data[1],
                z=accel_data[2]
            )

            # 자이로스코프 데이터
            gyro_data = data['gyro']['data'][-1][1]
            msg.angular_velocity = Vector3(
                x=gyro_data[0],
                y=gyro_data[1],
                z=gyro_data[2]
            )

            # 회전 벡터 데이터
            rot_data = data['rot_vector']['data'][-1][1]
            msg.orientation = Quaternion(
                x=rot_data[0],
                y=rot_data[1],
                z=rot_data[2],
                w=rot_data[3]
            )

            # 공분산 행렬 설정
            msg.orientation_covariance[0] = -1.0
            msg.angular_velocity_covariance[0] = -1.0
            msg.linear_acceleration_covariance[0] = -1.0

            self.publisher_.publish(msg)

        except Exception as e:
            self.get_logger().error(f"Error fetching or processing sensor data: {e}")


def main(args=None):
    parser = argparse.ArgumentParser(description='ROS2 IP Camera Streamer')
    parser.add_argument('--ip', type=str, required=True, help='IP address and port of the IP camera (e.g., 192.168.0.180:8080)')
    cli_args = parser.parse_args()

    rclpy.init(args=args)  # Initialize the ROS 2 Python client library
    node = IMUNode(cli_args.ip)  # Create an instance of the CameraNode with the IP address and port
    try:
        rclpy.spin(node)  # Spin the node to keep it alive and processing callbacks
    except KeyboardInterrupt:
        pass  # Allow the user to exit with Ctrl+C
    finally:
        node.destroy_node()  # Destroy the ROS 2 node
        rclpy.shutdown()  # Shut down the ROS 2 Python client library

if __name__ == '__main__':
    main()  # Run the main function if this script is executed
