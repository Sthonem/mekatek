import rclpy
from std_msgs.msg import String

def chatter_callback(msg):
    print('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('erdem_subscriber')

    subscription = node.create_subscription(String, 'Mekatek', chatter_callback, 10)
    subscription  # prevent unused variable warning

    node.get_logger().info('Listening for messages...')

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

