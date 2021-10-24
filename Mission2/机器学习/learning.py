import numpy as np
import tensorflow as tf

'''
0.00632  18.00   2.310  0  0.5380  6.5750  65.20  4.0900   1  296.0  15.30  396.90   4.98  24.00
0.02731   0.00   7.070  0  0.4690  6.4210  78.90  4.9671   2  242.0  17.80  396.90   9.14  21.60
'''
def normalize(X):
    mean = np.mean(X)
    std = np.std(X)
    X = (X - mean) / std
    return X


def mul_linear():
    boston = tf.contrib.learn.datasets.load_dataset('boston')
    X_train, Y_train = boston.data, boston.target
    X_train = normalize(X_train)

    m, n = X_train.shape[0], X_train.shape[1]

    X = tf.placeholder(tf.float32, name='X', shape=(m, n))
    Y = tf.placeholder(tf.float32, name='Y')

    W = tf.Variable(tf.random.normal([n, 1]), dtype=tf.float32)
    b = tf.Variable(np.random.randn(), dtype=tf.float32)

    Y_hat = tf.add(tf.matmul(X, W), b)

    loss = tf.reduce_mean(tf.square(Y_hat - Y, name='loss'))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.04).minimize(loss)

    init_op = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init_op)

        for i in range(3000):
            l, _, ww = sess.run([loss, optimizer, W], feed_dict={X: X_train, Y: Y_train})
            if i % 200 == 0:
                print("第 %d 次loss为: %f" %(i, l))
                print("第" + str(i) +"次W为: ", ww)

            if l < 0.00001:
                break

        print(W.eval())
        print(b.eval())
        Y_pred = tf.add(tf.matmul(X_train, tf.cast(W, dtype=tf.float64)), tf.cast(b, dtype=tf.float64))

        # 预测结果
        print("Y_pred top 10 is: ", Y_pred[0:10].eval())
        print("Y_train top 10 is: ", Y_train[0:10])

mul_linear()
