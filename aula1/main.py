from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate as ing
from scipy import optimize as opt

plt.rcParams.update({
    'text.usetex': True,
    'font.size': 16
})

def makeBuoyEffectFigure(N: int):
    fig, ax = plt.subplots()

    x = np.linspace(0, 1, N)
    y_pure = x
    y_buoy = x * 0.8

    ax.plot(x, y_pure, label=r'No $\vec{E}_{ar}$')
    ax.plot(x, y_buoy, label=r'With $\vec{E}_{ar}$')

    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$v$')

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.legend()

    ax.set_title('$v(t)$ por $t$')

    return fig


def makeDragEffectFigure(N: int):
    fig, ax = plt.subplots()

    x = np.linspace(0.0, 1.0, N)
    y_pure = x

    deriv = lambda t, u: (u[1], 1.0-1.0*u[1])
    u0 = (0.0, 0.0)
    sol = ing.solve_ivp(deriv, (0.0, 1.0), u0, t_eval=x)

    y_drag = sol.y[1]

    print(sol.y)

    ax.plot(x, y_pure, label=r'No $\vec{F}_d$')
    ax.plot(x, y_drag, label=r'With $\vec{F}_d$')

    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$v$')

    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)

    ax.set_xticks([])
    ax.set_yticks([])

    ax.legend()

    ax.set_title('$v(t)$ por $t$')

    return fig

fig_buoy = makeBuoyEffectFigure(100)
fig_drag = makeDragEffectFigure(100)
plt.show()