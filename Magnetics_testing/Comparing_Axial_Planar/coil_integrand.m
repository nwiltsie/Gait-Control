function y = coil_integrand(theta, x, R, I)
% y = (1 - x/R .* cos(theta)) ./ sqrt(x^2 ./ R^2 - 2 .* x / R .* cos(theta) + 1);
y = I * R^2 / (4 * pi) * (1 - x ./ R .* cos(theta)) ./ (x.^2 - 2 .* x .* R .* cos(theta) + R.^2).^(3/2);
