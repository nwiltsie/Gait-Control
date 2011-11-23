function B = solenoid_field(R, L, I, n, x)
% Field from a finite solenoid at a point x from the center along its axis
% R: radius, m
% L: length, m
% I: current, A
% n: number of turns
% x: axial position, m
%
% Returns:
% B: axial magnetic field, T

mu_0 = 4 * pi * 10^-7;

theta1 = atan2(R, L/2 - x);
theta2 = atan2(R, -(L/2 + x));
B = mu_0 .* I .* n ./ (2 .* L) .* (cos(theta1) - cos(theta2));
