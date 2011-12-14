function [power_W, copper_volume_m3] = helmholtz_power(wire_dia_in, num_turns)

inner_diameter_in = 1.5;
desired_field_T = 0.3;

wire_radius_m = wire_dia_in/2 * .0254;
bundle_radius_m = sqrt(num_turns ./ .9) .* (wire_radius_m);
helmholtz_radius_m = (inner_diameter_in./2) .* .0254 + bundle_radius_m;
current_A = desired_field_T .* helmholtz_radius_m ./ (1.26.*10^-6 .* num_turns) .* (4./5).^(-3/2);
coil_resistance_Ohm = num_turns .* 2 * pi .* helmholtz_radius_m ./ (pi .* wire_radius_m.^2) .* 1.7.*10.^-8;
voltage_V = current_A .* coil_resistance_Ohm;
power_W = voltage_V .* current_A;
copper_volume_m3 = pi .* wire_radius_m .^2 .* num_turns .* 2 .* pi .* helmholtz_radius_m;

