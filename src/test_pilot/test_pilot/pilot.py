import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):
    def __init__(self, name):
        super().__init__(name)
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Info received '{msg.data}'")


def main():
    rclpy.init()
    sub = MinimalSubscriber('test_pilot')

    rclpy.spin(sub)

    sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
