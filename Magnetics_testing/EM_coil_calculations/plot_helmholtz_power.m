[X, Y] = meshgrid(linspace(.02, .2), linspace(100, 2000));
[power_W, copper_volume_m3] = helmholtz_power(X, Y);

figure()
subplot 211
contourf(X, Y, power_W, 1000, 'LineStyle','none')
colorbar
xlabel('Wire diameter (in)')
ylabel('Number of turns')
title('Power (W)')

subplot 212
contourf(X, Y, copper_volume_m3, 1000, 'LineStyle','none')
colorbar
xlabel('Wire diameter (in)')
ylabel('Number of turns')
title('Copper Volume (m^3)')

% figure()
% contourf(X, Y, copper_volume_m3.*power_W, 1000, 'LineStyle','none')
% colorbar
% xlabel('Wire diameter (in)')
% ylabel('Number of turns')
% title('Copper Volume (m^3) * Power (W)')

