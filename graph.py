from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

df = D['ABEV3.SA'][-200:,0:8]
shape1,shape0 = [int(x) for x in df.shape ]

a=[]
for x in range(shape0):
    a.append(np.arange(0, shape1, 1.))
#    
X = np.vstack(a)

y = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
Y = np.repeat(y, X.shape[1],axis=1)

Z = df.T



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#X, Y, Z = axes3d.get_test_data(0.1)


ax.plot_wireframe(X, Y, Z, rstride=1, cstride=0, color = ['0.2','r','0.3','r','0.2'])

ax.set_title('Wavelets Retornos')
ax.set_xlabel('Dias')
ax.set_ylabel('j')
ax.set_zlabel('Retornos')
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.show()
    
#%%
#plt.plot(D['ABEV3.SA'][1])
#plt.plot(D['ABEV3.SA'][2])
#plt.plot(D['ABEV3.SA'][3])

#plt.plot(b[0], color = 'c')
         
#plt.show()

#
#plt.plot(b[1] ,color = 'g')
#plt.show()
#
#plt.plot(b[2] ,color = 'y')
#plt.show()
#
#plt.plot(b[3] ,color = 'r')
#plt.show()
#
#plt.plot(b[4] ,color = 'b')
#plt.show()
#
#plt.figure()
#plt.plot(b[8] ,color = 'r')
#plt.show()
#
#plt.plot(b[9] ,color = 'b')
#plt.show()
#plt.plot(b[7], color = 'g')
#         
#plt.show()
#
