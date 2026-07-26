import numpy as np

def _fade(t):
    return 6 * t**5 -15*t**4 + 10 * t**3

def _lerp(a,b,t):
    return a + t * (b-a)

def _gradient_vectors(shape,seed=None):
    rng = np.random.default_rng(seed)
    angles = rng.uniform(0,2*np.pi,size=shape)
    return np.dstack((np.cos(angles),np.sin(angles)))

def generate_perlin_noise_2d(width,height,cell_size,seed=None):
    grid_w = width//cell_size + 2
    grid_h = height//cell_size + 2
    gradients = _gradient_vectors((grid_h,grid_w),seed=seed)
    noise = np.zeros((height,width),dtype=np.float64)

    xs = np.arrange(width)
    ys = np.arrange(height)

    grid_x = xs//cell_size
    grid_y = ys//cell_size

    local_x = (xs%cell_size)/cell_size
    local_y = (ys%cell_size)/cell_size

    for row in range(height):
        gy = grid_y[row]
        ly = local_y[row]
        fy = _fade(ly)

        gx_row = grid_x
        lx_row = local_x

        g00 = gradients[gy,gx_row]
        g10 = gradients[gy,gx_row+1]
        g01 = gradients[gy + 1,gx_row]
        g11 = gradients[gy+1,gx_row + 1]

        d00 = np.stack((lx_row,np.full_like(lx_row,ly)))[0]
        d10 = np.dstack((lx_row-1,np.full_like(lx_row,ly)))[0]
        d01 = np.dstack((lx_row,np.full_like(lx_row,ly-1)))
        d11 = np.dstack((lx_row-1,np.full_like(lx_row,ly - 1)))[0]

        dot00 = np.sum(g00*d00,axis=1)
        dot10 = np.sum(g10*d10,axis=-1)
        dot01 = np.sum(g01*d01,axis=1)
        dot11 = np.sum(g11*d11,axis=-1)

        fx = _fade(lx_row)

        lerp_top = _lerp(dot00,dot10,fx)
        lerp_bottom = _lerp(dot01,dot11,fx)
        result = _lerp(lerp_top,lerp_bottom,fy)

        noise[row] = result

    max_val = np.max(np.abs(noise))
    if max_val > 0:
        noise = noise/max_val

    return noise

def generate_fractal_noise_2d(width,height,cell_size,octaves=4,persistence=0.5,lacunarity=2.0,seed=None):
    total = np.zeros((height,width),dtype=np.float64)
    amplitude = 1.0
    frequency_cell_size = cell_size
    max_amplitude = 0.0

    for octave in range(octaves):
        octave_seed = None if seed is None else seed + octave * 1000
        layer = generate_fractal_noise_2d(width,height,max(2,int(frequency_cell_size)),seed=octave_seed)
        
    total += layer * amplitude
    return total

def sample_grid(rows,cols,cell_size=4,octaves=3,persistence=0.5,lacunarity=2.0,seed=None):
    noise_map = generate_fractal_noise_2d(
        width=cols,height=rows,cell_size=cell_size, octaves=octaves,persistence=persistence,lacunarity=lacunarity,seed=seed

    )
    normalized = (noise_map - noise_map.min())/(noise_map.max()-noise_map.min()+1e-9)
    return normalized