import numpy as num

D = 10  # Maximum displacement
P = 11  # Period of the complete cycle
t0 = 1  # Time at which to reverse motion

# sample_range = num.linspace(0, 20, 101)
# print sample_range

def f(t):
    return D*t/t0
    
def g(t): 
    return D - D/(P-t0)*t
    
def get_desired_position(time):
    if time < t0:
        return f(time)
    else:
        return g(time)

# initialize PID Control
Kp = 1.0
Kd = 0.0
Ki = 0.0
accumulated_error = 0 # updated by integral error
time_started = 0 # get value from system clock
last_update = time_started # update when finished calculations


while True:
    # get current time
    # calculate delta_t
    # determine time location in this cycle, time %= period
    # calculate desired position
    # read actual position from encoder
    # determine current error
    # calculate proportional contribution
    # calculate differential contribution
    # update accumulated error
    # calculate integral contribution
    # determine total error
    # calculate output signal
    # housekeeping - update previous-error and latest time
    pass
    

