function generate_coil_axi()

wire_dia_m = 0.0641 * 0.0254;
coil_inner_r_m = 1.5 / 2 * 0.0254;
n = 400;

A = n * 1/0.9 * pi * (wire_dia_m / 2)^2;
bundle_r_m = sqrt(A / pi);

coil_center_r_m = coil_inner_r_m + bundle_r_m;

I_A = 22.28;

model_file = 'helmholtz_coil_axi.fem';

openfemm;

newdocument(0);
freq = 0;
units = 'meters';
type = 'axi';
precision = 1e-008;
depth = 0;
minangle = 30;
mi_probdef(freq, units, type, precision, depth, minangle);

%% Add the air material
matname = 'Air';
mu_x = 1;
mu_y = 1;
H_c = 0;
J = 0;
Cduct = 0;
Lam_d = 0;
Phi_hmax = 0;
lam_fill = 1;
LamType = 0;
Phi_hx = 0;
Phi_hy = 0;
mi_addmaterial(matname, mu_x, mu_y, H_c, J, Cduct, Lam_d, Phi_hmax, lam_fill, LamType, Phi_hx, Phi_hy);

%% Add the coil material
matname = 'copper_coil';
mu_x = 1;
mu_y = 1;
H_c = 0;
J = 0;
Cduct = 59; %Megasiemens per meter
Lam_d = 0;
Phi_hmax = 0;
lam_fill = 1;
LamType = 0;
Phi_hx = 0;
Phi_hy = 0;
mi_addmaterial(matname, mu_x, mu_y, H_c, J, Cduct, Lam_d, Phi_hmax, lam_fill, LamType, Phi_hx, Phi_hy);

%% Create the coil circuit
circuit_name = 'coil_circuit';
series = 1;
mi_addcircprop(circuit_name, I_A, series)

%% Define the MR fluid material
matname = 'LORD MRF 132-DG - mu=6';
mu_x = 6;
mu_y = 6;
H_c = 0;
J = 0;
Cduct = 0; %Megasiemens per meter
Lam_d = 0;
Phi_hmax = 0;
lam_fill = 1;
LamType = 0;
Phi_hx = 0;
Phi_hy = 0;
mi_addmaterial(matname, mu_x, mu_y, H_c, J, Cduct, Lam_d, Phi_hmax, lam_fill, LamType, Phi_hx, Phi_hy);
MRF_BH = 	[0, 0;
0.10315186246418299, 12098.2986767486;
0.16045845272206299, 19659.7353497164;
0.229226361031519, 30245.7466918715;
0.30945558739255002, 43856.3327032136;
0.37249283667621802, 57466.918714555803;
0.424068767908309, 66540.642722117205;
0.48137535816618898, 80151.2287334594;
0.555873925501433, 95274.102079395103;
0.60744985673352403, 116446.124763705;
0.68194842406876799, 139130.43478260899;
0.722063037249284, 154253.30812854401;
0.78510028653295105, 178449.905482042;
0.83094555873925502, 198109.64083175801;
0.87679083094555899, 222306.238185255;
0.916905444126075, 243478.26086956501;
0.95128939828080195, 263137.99621928198;
0.97421203438395398, 279773.156899811;
0.99713467048710602, 290359.16824196599];
for i = 1:length(MRF_BH(:,1))
	mi_addbhpoint(matname, MRF_BH(i, 1), MRF_BH(i, 2));
end

%% Set up the boundary
mi_addboundprop('boundary', 0, 0, 0, 0, 0, 0, 0, 0, 4); % periodic boundary

%% Draw the coils
top_coil_center = [coil_center_r_m, coil_center_r_m / 2];
bottom_coil_center = [coil_center_r_m, -coil_center_r_m / 2];

TC_1 = top_coil_center + [0, -bundle_r_m];
TC_2 = top_coil_center + [0, bundle_r_m];

BC_1 = bottom_coil_center + [0, -bundle_r_m];
BC_2 = bottom_coil_center + [0, bundle_r_m];

mi_addnode(TC_1(1), TC_1(2));
mi_addnode(TC_2(1), TC_2(2));
mi_addnode(BC_1(1), BC_1(2));
mi_addnode(BC_2(1), BC_2(2));

mi_addarc(TC_1(1), TC_1(2), TC_2(1), TC_2(2), 180, 1);
mi_addarc(TC_2(1), TC_2(2), TC_1(1), TC_1(2), 180, 1);
mi_addarc(BC_1(1), BC_1(2), BC_2(1), BC_2(2), 180, 1);
mi_addarc(BC_2(1), BC_2(2), BC_1(1), BC_1(2), 180, 1);

%% Draw the boundary
bound_top = [0, coil_center_r_m * 2];
bound_bottom = [0, -coil_center_r_m * 2];

mi_addnode(bound_top(1), bound_top(2));
mi_addnode(bound_bottom(1), bound_bottom(2));
mi_addarc(bound_bottom(1), bound_bottom(2), bound_top(1), bound_top(2), 180, 1);
mi_selectarcsegment(bound_top(1), bound_top(2));
mi_setarcsegmentprop(1, 'boundary', 0, 0);
mi_clearselected;
mi_addsegment(bound_bottom(1), bound_bottom(2), bound_top(1), bound_top(2));

%% Fill the empty space with air
mi_addblocklabel(0.001, -coil_center_r_m);
mi_selectlabel(0.001, -coil_center_r_m);

blockname = 'Air';
automesh = 1;
meshsize = 0;
incircuit = 0;
magdir = 0;
group = 1;
turns = 0;
mi_setblockprop(blockname, automesh, meshsize, incircuit, magdir, group, turns);
mi_clearselected;

%% Add the MRF
fluid_radius_m = 0.5 * 0.0254;
fluid_thickness_m = 0.125 * 0.0254;

MRF_1 = [fluid_radius_m, fluid_thickness_m / 2];
MRF_2 = [0, fluid_thickness_m / 2];
MRF_3 = [0, -fluid_thickness_m / 2];
MRF_4 = [fluid_radius_m, -fluid_thickness_m / 2];

mi_addnode(MRF_1(1), MRF_1(2));
mi_addnode(MRF_2(1), MRF_2(2));
mi_addnode(MRF_3(1), MRF_3(2));
mi_addnode(MRF_4(1), MRF_4(2));
mi_drawpolygon([MRF_1(1), MRF_1(2); MRF_2(1), MRF_2(2); MRF_3(1), MRF_3(2); MRF_4(1), MRF_4(2)]);

mi_addblocklabel(fluid_radius_m / 2, 0);
mi_selectlabel(fluid_radius_m /2, 0);
blockname = 'LORD MRF 132-DG - mu=6';
automesh = 1;
meshsize = 0;
incircuit = 0;
magdir = 0;
group = 3;
turns = 0;
mi_setblockprop(blockname, automesh, meshsize, incircuit, magdir, group, turns);
mi_clearselected;


%% Energize the coils
mi_addblocklabel(top_coil_center(1), top_coil_center(2));
mi_selectlabel(top_coil_center(1), top_coil_center(2));
blockname = 'copper_coil';
automesh = 1;
meshsize = 0;
incircuit = 'coil_circuit';
magdir = 0;
group = 1;
turns = n;
mi_setblockprop(blockname, automesh, meshsize, incircuit, magdir, group, turns);
mi_clearselected;

mi_addblocklabel(bottom_coil_center(1), bottom_coil_center(2));
mi_selectlabel(bottom_coil_center(1), bottom_coil_center(2));
mi_setblockprop(blockname, automesh, meshsize, incircuit, magdir, group, turns);
mi_clearselected;

mi_saveas(model_file);
mi_zoomnatural;
mi_refreshview;



