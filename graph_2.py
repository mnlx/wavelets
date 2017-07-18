df = D['ABEV3.SA'][-20:,0:8]
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
ax = fig.gca(projection='3d')               # 3d axes instance
surf = ax.plot_surface(X, Y, Z,             # data values (2D Arryas)
                       rstride=2,           # row step size
                       cstride=2,           # column step size
                       cmap=cm.RdPu,        # colour map
                       linewidth=1,         # wireframe line width
                       antialiased=True)



ax.zaxis.set_major_locator(LinearLocator(6))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_title('Hyperbolic Paraboloid')        # title
fig.colorbar(surf, shrink=0.5, aspect=5)     # colour bar

ax.view_init(elev=30,azim=70)                # elevation & angle
ax.dist=8                                    # distance from the plot
plt.show()