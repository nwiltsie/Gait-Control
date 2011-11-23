function B = helmholtz_field(R, I, n, x)
% Field from a finite helmholtz coil at a point x from the center along its axis
% R: radius, m
% I: current, A
% n: number of turns
% x: axial position, m
%
% Returns:
% B: axial magnetic field, T

mu_0 = 4 * pi * 10^-7;

B = n .* R^2 .* I * mu_0 .*...
	(1 ./ (2 .* (R^2 + (R/2 + x).^2).^(3/2))...
   + 1 ./ (2 .* (R^2 + (R/2 - x).^2).^(3/2)));
