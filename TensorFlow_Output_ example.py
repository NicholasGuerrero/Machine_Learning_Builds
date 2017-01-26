import tensorflow as tf

# creates nodes in a graph
# "construction phase"
x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.mul(x1,x2)
print(result)

# defines our session and launches graph
sess = tf.Session()
# runs result and then closes the session
print(sess.run(result))
sess.close()

#another option (must open session again)
output = sess.run(result)
print(output)


#another option
with tf.Session() as sess:
    output = sess.run(result)
    print(output)
