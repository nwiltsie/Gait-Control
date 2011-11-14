D = 100;
I = 1;


R = D;
x = linspace(-D, D, 1000);
H_wire = I ./ (pi * D * (1 - x.^2 ./ D^2));

H_coil = zeros(length(x));
for i = 1:length(x)
	F = @(theta) coil_integrand(theta, x(i), R, I);
	H_coil(i) = quadl(F, 0, 2*pi);
end

figure
plot(x, H_wire, x, H_coil);
legend('Wire', 'Coil')
