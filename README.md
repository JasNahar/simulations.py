Star System Simulation (Python + Pygame)

A real-time physics simulation that models the motion of celestial bodies under gravitational and electrostatic forces. The system simulates a central massive body (star-like) and multiple interacting particles, visualized dynamically using Pygame.

Features
Multi-body simulation with gravity and charge-based interactions
Central massive body influencing surrounding particles
Real-time motion using time-step integration
Object-Oriented Design (Body, BlackHole)
Dynamic visualization of orbital behavior
Physics Model (Simplified)
Gravitational force:
Fg = (G * m1 * m2) / (r^2)
Electrostatic force:
Fe = (k * q1 * q2) / (r^2)
Acceleration:
a = F / m
Motion update (per time step dt):
x = x + vx * dt + 0.5 * ax * dt^2
y = y + vy * dt + 0.5 * ay * dt^2
vx = vx + ax * dt
vy = vy + ay * dt
Central body behavior:
Objects entering a defined radius are removed (collision/absorption approximation)
Tech Stack
Python
Pygame
Mathematics (Physics Simulation, Numerical Methods)
