% Plot the axial field for a finite solenoid and a helmholtz coil to compare their relative magnetic field strengths

R_sol_m = 1; % solenoid radius, meters
L_sol_m = R_sol_m; % solenoid length, meters
I_sol_A = 1; % solenoid current, Amps
n_sol = 1000; % solenoid number of turns

R_hel_m = R_sol_m; % helmholtz coil radius, meters
I_hel_A = I_sol_A;
n_hel = n_sol / 2;

x = linspace(-R_hel_m / 2, R_hel_m / 2, 1000);
% x = linspace(-7, 7, 1000);

% theta1 = atan2(R_sol_m, L_sol_m/2 - x);
% theta2 = atan2(R_sol_m, -(L_sol_m/2 + x));

% mu_0 = 4 * pi * 10^-7;

% B_sol_1 = mu_0 .* I_sol_A .* n_sol ./ (2 .* L_sol_m) .* (cos(theta1) - cos(theta2));

% B_hel = n_hel .* R_hel_m^2 .* I_hel_A * mu_0 .*...
%     (1 ./ (2 .* (R_hel_m^2 + (R_hel_m/2 + x).^2).^(3/2))...
%    + 1 ./ (2 .* (R_hel_m^2 + (R_hel_m/2 - x).^2).^(3/2)));

B_sol_1 = solenoid_field(R_sol_m, L_sol_m, I_sol_A, n_sol, x);
B_sol_2 = solenoid_field(R_sol_m, L_sol_m * 2, I_sol_A, n_sol, x);
B_sol_4 = solenoid_field(R_sol_m, L_sol_m * 4, I_sol_A, n_sol, x);
B_hel = helmholtz_field(R_hel_m, I_hel_A, n_hel, x);

figure()
B_sol_ideal = mu_0 * n_sol * I_sol_A / L_sol_m; % magnetic field from an infinite solenoid
B_hel_center = (4/5)^(3/2) * mu_0 * n_hel * I_hel_A / R_hel_m;
subplot 211
hold on
plot(x, B_sol_1, 'Color',[1 0 0])
plot(x, B_sol_2, 'Color', [1 0 1])
plot(x, B_sol_4, 'Color', [0 0 1])
plot(x, B_hel,'g-')
legend('Solenoid, L=R', 'Solenoid, L=2R', 'Solenoid, L=4R', 'Helmholtz')
xlabel('Axial position from center (m)')
ylabel('Axial magnetic field (T)')

subplot 212
hold on
plot(x, B_sol_1/max(B_sol_1), 'Color', [1 0 0])
plot(x, B_sol_2/max(B_sol_2), 'Color', [1 0 1])
plot(x, B_sol_4/max(B_sol_4), 'Color', [0 0 1])
plot(x, B_hel/max(B_hel), 'g-')
legend('Solenoid, L=R', 'Solenoid, L=2R', 'Solenoid, L=4R', 'Helmholtz')
xlabel('Axial position from center (m)')
ylabel('Fraction of maximum field')

