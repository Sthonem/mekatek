import rclpy
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('erdem_publisher')

    publisher = node.create_publisher(String, 'Mekatek', 10)
    msg = String()

    count = 0
    while rclpy.ok():
        msg.data = 'Hello Mekatek: %d' % count
        node.get_logger().info('Publishing: "%s"' % msg.data)
        publisher.publish(msg)
        count += 1
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

