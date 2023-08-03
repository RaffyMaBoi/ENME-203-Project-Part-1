import matplotlib.pyplot as plt
import numpy as np

l = 5
lc = 4
d = 3
W = np.pi/10
t = 10


def data():
    "Retreives arrays form file given"
    t = np.loadtxt('trailer.csv', delimiter=',', usecols =0)
    phi = np.loadtxt('trailer.csv', delimiter=',', usecols =1)
    dphi = np.loadtxt('trailer.csv', delimiter=',', usecols =2)
    ddphi = np.loadtxt('trailer.csv', delimiter=',', usecols =3)
    
    return t, phi, dphi, ddphi 
    

def abs_velocity(t, phi, dphi):
    "Plots absolute velocity against data"
    
    Absolute_Vc = np.sqrt((lc*dphi*np.sin(phi))**2+(((-W*d)/2)*np.sin(W*t)-lc*dphi*np.cos(phi))**2)
    Absolute_Va = np.sqrt(((-d*W/2)*(np.sin(W*t)))**2)
    
    axes = plt.axes()
    
    axes.plot(t,  Absolute_Vc, label = 'Absolute_Vc')
    axes.plot(t,  Absolute_Va, label = 'Absolute_Va')
    axes.set_title('Absolute Velocity of A and C over 10[s]')
    axes.set_xlabel('Time [s]')
    axes.set_ylabel('Velocity [m/s]')
    axes.legend()
    
    axes.grid(True)
    plt.show()

    
def velocity_comp(t, phi, dphi):
    "Plots velocity components"
    
    Va_x = np.zeros((100))
    Va_y =(-d*W/2)*(np.sin(W*t))
    Vc_x =lc*dphi*np.sin(phi)
    Vc_y =((-W*d)/2)*np.sin(W*t)-lc*dphi*np.cos(phi)
    
    axes = plt.axes()
    
    axes.plot(t,  Va_x, label = 'Va_x')
    axes.plot(t,  Va_y, label = 'Va_y')
    axes.plot(t,  Vc_x, label = 'Vc_x')
    axes.plot(t,  Vc_y, label = 'Vc_y')
    
    axes.set_title('Directional Velocity Components of A and C over 10[s]')
    axes.set_xlabel('Time [s]')
    axes.set_ylabel('Velocity [m/s]')
    axes.legend()
    
    axes.grid(True)
    plt.show()
 
    
def abs_acceleration(t, phi, dphi, ddphi ):
    "Plots Acceleration againsts data"
    
    A_x = (lc*ddphi*np.sin(phi)) + (lc*dphi**2*np.cos(phi))
    A_y =( -(d*W**2/2)*np.cos(W*t)) + (-lc*ddphi*np.cos(phi)) + (lc*dphi**2*np.sin(phi)) 
    Absolute_Ac = np.sqrt((A_x)**2+(A_y)**2)
    
    axes = plt.axes()
    
    axes.plot(t,  Absolute_Ac, label = 'Absolute_Acceleration of C')
    axes.set_title('Absolute Acceleration of C over 10[s]')
    axes.set_xlabel('Time [s]')
    axes.set_ylabel('Acceleration [m/s^2]')
    axes.legend()
    
    axes.grid(True)
    plt.show()
    
    
def acceleration_comp(t, phi, dphi, ddphi ):
    "Plots velocity components"
    
    Ac_x = (lc*ddphi*np.sin(phi)) + (lc*dphi**2*np.cos(phi))
    Ac_y =( -(d*W**2/2)*np.cos(W*t)) + (-lc*ddphi*np.cos(phi)) + (lc*dphi**2*np.sin(phi)) 
    
    axes = plt.axes()
    
    axes.plot(t,  Ac_x, label = 'Acceleration in x')
    axes.plot(t,  Ac_y, label = 'Acceleration in y')
    
    axes.set_title('Directional Acceleration Components of C over 10[s]')
    axes.set_xlabel('Time [s]')
    axes.set_ylabel('Acceleration [m/s^2]')
    axes.legend()
    
    axes.grid(True)
    plt.show()
    

def main():
    "Main Function"
    
    "Gets Data from File"
    t, phi, dphi, ddphi = data()
            
    "Plots Absolute Velocity"
    #abs_velocity(t, phi, dphi)
    
    "Plots Velocity Components"
    #velocity_comp(t, phi, dphi,)
       
    "Plots Absulute Acceleration"
    #abs_acceleration(t, phi, dphi, ddphi)
      
    "Plots Acceleration Components"
    acceleration_comp(t, phi, dphi, ddphi)

main()        
    