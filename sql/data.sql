INSERT INTO eglise (nom, argent) VALUES
('Église Saint-Jean', 10000.00),
('Église Sainte-Marie', 15000.00),
('Église Saint-Pierre', 20000.00),
('Église Saint-Paul', 18000.00),
('Église Sainte-Anne', 12000.00);


-- Insérer 5 croyants pour chaque église
INSERT INTO croyant (nom, id_eglise, login, mdp, statut) VALUES
-- Église Saint-Jean
('Jean Dupont', 1, 'jean.dupont', 'password1', 'croyant'),
('Marie Martin', 1, 'marie.martin', 'password2', 'croyant'),
('Pierre Dubois', 1, 'pierre.dubois', 'password3', 'croyant'),
('Sophie Lambert', 1, 'sophie.lambert', 'password4', 'pasteur'),
('Nicolas Girard', 1, 'nicolas.girard', 'password5', 'pasteur'),

-- Église Sainte-Marie
('Lucie Tremblay', 2, 'lucie.tremblay', 'password6', 'croyant'),
('Michel Gagnon', 2, 'michel.gagnon', 'password7', 'croyant'),
('Isabelle Roy', 2, 'isabelle.roy', 'password8', 'croyant'),
('Éric Lavoie', 2, 'eric.lavoie', 'password9', 'pasteur'),
('Julie Bergeron', 2, 'julie.bergeron', 'password10', 'pasteur'),

-- Église Saint-Pierre
('Sylvie Bouchard', 3, 'sylvie.bouchard', 'password11', 'croyant'),
('David Leblanc', 3, 'david.leblanc', 'password12', 'croyant'),
('Caroline Fortin', 3, 'caroline.fortin', 'password13', 'croyant'),
('Martin Morin', 3, 'martin.morin', 'password14', 'pasteur'),
('Valérie Gagné', 3, 'valerie.gagne', 'password15', 'pasteur'),

-- Église Saint-Paul
('Stéphanie Parent', 4, 'stephanie.parent', 'password16', 'croyant'),
('Patrick Bélanger', 4, 'patrick.belanger', 'password17', 'croyant'),
('Annie Lemieux', 4, 'annie.lemieux', 'password18', 'croyant'),
('Alexandre Dubé', 4, 'alexandre.dube', 'password19', 'pasteur'),
('Catherine Lévesque', 4, 'catherine.levesque', 'password20', 'pasteur'),

-- Église Sainte-Anne
('Marcelle Pelletier', 5, 'marcelle.pelletier', 'password21', 'croyant'),
('Paul Lachance', 5, 'paul.lachance', 'password22', 'croyant'),
('Louise Bernard', 5, 'louise.bernard', 'password23', 'croyant'),
('Gilles Lefebvre', 5, 'gilles.lefebvre', 'password24', 'pasteur'),
('Martine Fortier', 5, 'martine.fortier', 'password25', 'pasteur');

INSERT INTO situation (id_croyant, matrimoniale, bapteme, communion) VALUES
(1, 'celibataire', NULL, NULL),
(2, 'marie(e)', '2023-01-01', '2023-01-01'),
(3, 'marie(e)', '2023-01-01', NULL),
(4, 'celibataire','2023-01-01', '2023-01-01'),
(5, 'celibataire', NULL, '2023-01-01');





-- Insérer des données pour chaque dimanche de chaque mois de l'année 2022 dans la table caisse

-- Janvier
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-01-02'),
(1, 18000.50, '2022-01-09'),
(1, 32000.25, '2022-01-16'),
(1, 15000.80, '2022-01-23'),
(1, 41000.60, '2022-01-30'),

-- Église 2
(2, 38000.35, '2022-01-02'),
(2, 29000.45, '2022-01-09'),
(2, 48000.70, '2022-01-16'),
(2, 42000.25, '2022-01-23'),
(2, 20000.90, '2022-01-30'),

-- Église 3
(3, 42000.25, '2022-01-02'),
(3, 35000.80, '2022-01-09'),
(3, 29000.55, '2022-01-16'),
(3, 18000.70, '2022-01-23'),
(3, 47000.40, '2022-01-30'),

-- Église 4
(4, 15000.90, '2022-01-02'),
(4, 41000.25, '2022-01-09'),
(4, 32000.60, '2022-01-16'),
(4, 28000.75, '2022-01-23'),
(4, 39000.40, '2022-01-30'),

-- Église 5
(5, 27000.40, '2022-01-02'),
(5, 38000.65, '2022-01-09'),
(5, 45000.30, '2022-01-16'),
(5, 21000.75, '2022-01-23'),
(5, 32000.50, '2022-01-30');

-- Février
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 32000.45, '2022-02-06'),
(1, 18000.60, '2022-02-13'),
(1, 25000.85, '2022-02-20'),
(1, 41000.20, '2022-02-27'),

-- Église 2
(2, 48000.50, '2022-02-06'),
(2, 29000.75, '2022-02-13'),
(2, 38000.30, '2022-02-20'),
(2, 20000.65, '2022-02-27'),

-- Église 3
(3, 29000.70, '2022-02-06'),
(3, 42000.35, '2022-02-13'),
(3, 47000.90, '2022-02-20'),
(3, 35000.25, '2022-02-27'),

-- Église 4
(4, 32000.80, '2022-02-06'),
(4, 41000.15, '2022-02-13'),
(4, 15000.50, '2022-02-20'),
(4, 28000.95, '2022-02-27'),

-- Église 5
(5, 45000.60, '2022-02-06'),
(5, 27000.85, '2022-02-13'),
(5, 32000.20, '2022-02-20'),
(5, 38000.75, '2022-02-27');

-- Continuez de la même manière pour les autres mois de l'année 2022


-- Mars
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-03-06'),
(1, 18000.50, '2022-03-13'),
(1, 32000.25, '2022-03-20'),
(1, 15000.80, '2022-03-27'),

-- Église 2
(2, 38000.35, '2022-03-06'),
(2, 29000.45, '2022-03-13'),
(2, 48000.70, '2022-03-20'),
(2, 42000.25, '2022-03-27'),

-- Église 3
(3, 42000.25, '2022-03-06'),
(3, 35000.80, '2022-03-13'),
(3, 29000.55, '2022-03-20'),
(3, 18000.70, '2022-03-27'),

-- Église 4
(4, 15000.90, '2022-03-06'),
(4, 41000.25, '2022-03-13'),
(4, 32000.60, '2022-03-20'),
(4, 28000.75, '2022-03-27'),

-- Église 5
(5, 27000.40, '2022-03-06'),
(5, 38000.65, '2022-03-13'),
(5, 45000.30, '2022-03-20'),
(5, 21000.75, '2022-03-27');

-- Avril
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-04-03'),
(1, 18000.50, '2022-04-10'),
(1, 32000.25, '2022-04-17'),
(1, 15000.80, '2022-04-24'),

-- Église 2
(2, 38000.35, '2022-04-03'),
(2, 29000.45, '2022-04-10'),
(2, 48000.70, '2022-04-17'),
(2, 42000.25, '2022-04-24'),

-- Église 3
(3, 42000.25, '2022-04-03'),
(3, 35000.80, '2022-04-10'),
(3, 29000.55, '2022-04-17'),
(3, 18000.70, '2022-04-24'),

-- Église 4
(4, 15000.90, '2022-04-03'),
(4, 41000.25, '2022-04-10'),
(4, 32000.60, '2022-04-17'),
(4, 28000.75, '2022-04-24'),

-- Église 5
(5, 27000.40, '2022-04-03'),
(5, 38000.65, '2022-04-10'),
(5, 45000.30, '2022-04-17'),
(5, 21000.75, '2022-04-24');

-- Continuez de la même manière pour les autres mois

-- Mai
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-05-01'),
(1, 18000.50, '2022-05-08'),
(1, 32000.25, '2022-05-15'),
(1, 15000.80, '2022-05-22'),
(1, 41000.60, '2022-05-29'),

-- Église 2
(2, 38000.35, '2022-05-01'),
(2, 29000.45, '2022-05-08'),
(2, 48000.70, '2022-05-15'),
(2, 42000.25, '2022-05-22'),
(2, 20000.90, '2022-05-29'),

-- Église 3
(3, 42000.25, '2022-05-01'),
(3, 35000.80, '2022-05-08'),
(3, 29000.55, '2022-05-15'),
(3, 18000.70, '2022-05-22'),
(3, 47000.40, '2022-05-29'),

-- Église 4
(4, 15000.90, '2022-05-01'),
(4, 41000.25, '2022-05-08'),
(4, 32000.60, '2022-05-15'),
(4, 28000.75, '2022-05-22'),
(4, 39000.40, '2022-05-29'),

-- Église 5
(5, 27000.40, '2022-05-01'),
(5, 38000.65, '2022-05-08'),
(5, 45000.30, '2022-05-15'),
(5, 21000.75, '2022-05-22'),
(5, 32000.50, '2022-05-29');

-- Juin
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-06-05'),
(1, 18000.50, '2022-06-12'),
(1, 32000.25, '2022-06-19'),
(1, 15000.80, '2022-06-26'),

-- Église 2
(2, 38000.35, '2022-06-05'),
(2, 29000.45, '2022-06-12'),
(2, 48000.70, '2022-06-19'),
(2, 42000.25, '2022-06-26'),

-- Église 3
(3, 42000.25, '2022-06-05'),
(3, 35000.80, '2022-06-12'),
(3, 29000.55, '2022-06-19'),
(3, 18000.70, '2022-06-26'),

-- Église 4
(4, 15000.90, '2022-06-05'),
(4, 41000.25, '2022-06-12'),
(4, 32000.60, '2022-06-19'),
(4, 28000.75, '2022-06-26'),

-- Église 5
(5, 27000.40, '2022-06-05'),
(5, 38000.65, '2022-06-12'),
(5, 45000.30, '2022-06-19'),
(5, 21000.75, '2022-06-26');

-- Continuez de la même manière pour les mois restants

-- Juillet
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-07-03'),
(1, 18000.50, '2022-07-10'),
(1, 32000.25, '2022-07-17'),
(1, 15000.80, '2022-07-24'),
(1, 41000.60, '2022-07-31'),

-- Église 2
(2, 38000.35, '2022-07-03'),
(2, 29000.45, '2022-07-10'),
(2, 48000.70, '2022-07-17'),
(2, 42000.25, '2022-07-24'),
(2, 20000.90, '2022-07-31'),

-- Église 3
(3, 42000.25, '2022-07-03'),
(3, 35000.80, '2022-07-10'),
(3, 29000.55, '2022-07-17'),
(3, 18000.70, '2022-07-24'),
(3, 47000.40, '2022-07-31'),

-- Église 4
(4, 15000.90, '2022-07-03'),
(4, 41000.25, '2022-07-10'),
(4, 32000.60, '2022-07-17'),
(4, 28000.75, '2022-07-24'),
(4, 39000.40, '2022-07-31'),

-- Église 5
(5, 27000.40, '2022-07-03'),
(5, 38000.65, '2022-07-10'),
(5, 45000.30, '2022-07-17'),
(5, 21000.75, '2022-07-24'),
(5, 32000.50, '2022-07-31');

-- Août
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-08-07'),
(1, 18000.50, '2022-08-14'),
(1, 32000.25, '2022-08-21'),
(1, 15000.80, '2022-08-28'),

-- Église 2
(2, 38000.35, '2022-08-07'),
(2, 29000.45, '2022-08-14'),
(2, 48000.70, '2022-08-21'),
(2, 42000.25, '2022-08-28'),

-- Église 3
(3, 42000.25, '2022-08-07'),
(3, 35000.80, '2022-08-14'),
(3, 29000.55, '2022-08-21'),
(3, 18000.70, '2022-08-28'),

-- Église 4
(4, 15000.90, '2022-08-07'),
(4, 41000.25, '2022-08-14'),
(4, 32000.60, '2022-08-21'),
(4, 28000.75, '2022-08-28'),

-- Église 5
(5, 27000.40, '2022-08-07'),
(5, 38000.65, '2022-08-14'),
(5, 45000.30, '2022-08-21'),
(5, 21000.75, '2022-08-28');

-- Continuez de la même manière pour les autres mois


-- Septembre
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-09-04'),
(1, 18000.50, '2022-09-11'),
(1, 32000.25, '2022-09-18'),
(1, 15000.80, '2022-09-25'),

-- Église 2
(2, 38000.35, '2022-09-04'),
(2, 29000.45, '2022-09-11'),
(2, 48000.70, '2022-09-18'),
(2, 42000.25, '2022-09-25'),

-- Église 3
(3, 42000.25, '2022-09-04'),
(3, 35000.80, '2022-09-11'),
(3, 29000.55, '2022-09-18'),
(3, 18000.70, '2022-09-25'),

-- Église 4
(4, 15000.90, '2022-09-04'),
(4, 41000.25, '2022-09-11'),
(4, 32000.60, '2022-09-18'),
(4, 28000.75, '2022-09-25'),

-- Église 5
(5, 27000.40, '2022-09-04'),
(5, 38000.65, '2022-09-11'),
(5, 45000.30, '2022-09-18'),
(5, 21000.75, '2022-09-25');

-- Octobre
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-10-02'),
(1, 18000.50, '2022-10-09'),
(1, 32000.25, '2022-10-16'),
(1, 15000.80, '2022-10-23'),
(1, 41000.60, '2022-10-30'),

-- Église 2
(2, 38000.35, '2022-10-02'),
(2, 29000.45, '2022-10-09'),
(2, 48000.70, '2022-10-16'),
(2, 42000.25, '2022-10-23'),
(2, 20000.90, '2022-10-30'),

-- Église 3
(3, 42000.25, '2022-10-02'),
(3, 35000.80, '2022-10-09'),
(3, 29000.55, '2022-10-16'),
(3, 18000.70, '2022-10-23'),
(3, 47000.40, '2022-10-30'),

-- Église 4
(4, 15000.90, '2022-10-02'),
(4, 41000.25, '2022-10-09'),
(4, 32000.60, '2022-10-16'),
(4, 28000.75, '2022-10-23'),
(4, 39000.40, '2022-10-30'),

-- Église 5
(5, 27000.40, '2022-10-02'),
(5, 38000.65, '2022-10-09'),
(5, 45000.30, '2022-10-16'),
(5, 21000.75, '2022-10-23'),
(5, 32000.50, '2022-10-30');

-- Continuez de la même manière pour les autres mois


-- Novembre
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-11-06'),
(1, 18000.50, '2022-11-13'),
(1, 32000.25, '2022-11-20'),
(1, 15000.80, '2022-11-27'),

-- Église 2
(2, 38000.35, '2022-11-06'),
(2, 29000.45, '2022-11-13'),
(2, 48000.70, '2022-11-20'),
(2, 42000.25, '2022-11-27'),

-- Église 3
(3, 42000.25, '2022-11-06'),
(3, 35000.80, '2022-11-13'),
(3, 29000.55, '2022-11-20'),
(3, 18000.70, '2022-11-27'),

-- Église 4
(4, 15000.90, '2022-11-06'),
(4, 41000.25, '2022-11-13'),
(4, 32000.60, '2022-11-20'),
(4, 28000.75, '2022-11-27'),

-- Église 5
(5, 27000.40, '2022-11-06'),
(5, 38000.65, '2022-11-13'),
(5, 45000.30, '2022-11-20'),
(5, 21000.75, '2022-11-27');

-- Décembre
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2022-12-04'),
(1, 18000.50, '2022-12-11'),
(1, 32000.25, '2022-12-18'),
(1, 15000.80, '2022-12-25'),

-- Église 2
(2, 38000.35, '2022-12-04'),
(2, 29000.45, '2022-12-11'),
(2, 48000.70, '2022-12-18'),
(2, 42000.25, '2022-12-25'),

-- Église 3
(3, 42000.25, '2022-12-04'),
(3, 35000.80, '2022-12-11'),
(3, 29000.55, '2022-12-18'),
(3, 18000.70, '2022-12-25'),

-- Église 4
(4, 15000.90, '2022-12-04'),
(4, 41000.25, '2022-12-11'),
(4, 32000.60, '2022-12-18'),
(4, 28000.75, '2022-12-25'),

-- Église 5
(5, 27000.40, '2022-12-04'),
(5, 38000.65, '2022-12-11'),
(5, 45000.30, '2022-12-18'),
(5, 21000.75, '2022-12-25');

-- Continuez de la même manière pour les autres mois


-- Janvier 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-01-01'),
(1, 18000.50, '2023-01-08'),
(1, 32000.25, '2023-01-15'),
(1, 15000.80, '2023-01-22'),
(1, 41000.60, '2023-01-29'),

-- Église 2
(2, 38000.35, '2023-01-01'),
(2, 29000.45, '2023-01-08'),
(2, 48000.70, '2023-01-15'),
(2, 42000.25, '2023-01-22'),
(2, 20000.90, '2023-01-29'),

-- Église 3
(3, 42000.25, '2023-01-01'),
(3, 35000.80, '2023-01-08'),
(3, 29000.55, '2023-01-15'),
(3, 18000.70, '2023-01-22'),
(3, 47000.40, '2023-01-29'),

-- Église 4
(4, 15000.90, '2023-01-01'),
(4, 41000.25, '2023-01-08'),
(4, 32000.60, '2023-01-15'),
(4, 28000.75, '2023-01-22'),
(4, 39000.40, '2023-01-29'),

-- Église 5
(5, 27000.40, '2023-01-01'),
(5, 38000.65, '2023-01-08'),
(5, 45000.30, '2023-01-15'),
(5, 21000.75, '2023-01-22'),
(5, 32000.50, '2023-01-29');

-- Février 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-02-05'),
(1, 18000.50, '2023-02-12'),
(1, 32000.25, '2023-02-19'),
(1, 15000.80, '2023-02-26'),

-- Église 2
(2, 38000.35, '2023-02-05'),
(2, 29000.45, '2023-02-12'),
(2, 48000.70, '2023-02-19'),
(2, 42000.25, '2023-02-26'),

-- Église 3
(3, 42000.25, '2023-02-05'),
(3, 35000.80, '2023-02-12'),
(3, 29000.55, '2023-02-19'),
(3, 18000.70, '2023-02-26'),

-- Église 4
(4, 15000.90, '2023-02-05'),
(4, 41000.25, '2023-02-12'),
(4, 32000.60, '2023-02-19'),
(4, 28000.75, '2023-02-26'),

-- Église 5
(5, 27000.40, '2023-02-05'),
(5, 38000.65, '2023-02-12'),
(5, 45000.30, '2023-02-19'),
(5, 21000.75, '2023-02-26');

-- Continuez de la même manière pour les autres mois

-- Mars 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-03-05'),
(1, 18000.50, '2023-03-12'),
(1, 32000.25, '2023-03-19'),
(1, 15000.80, '2023-03-26'),

-- Église 2
(2, 38000.35, '2023-03-05'),
(2, 29000.45, '2023-03-12'),
(2, 48000.70, '2023-03-19'),
(2, 42000.25, '2023-03-26'),

-- Église 3
(3, 42000.25, '2023-03-05'),
(3, 35000.80, '2023-03-12'),
(3, 29000.55, '2023-03-19'),
(3, 18000.70, '2023-03-26'),

-- Église 4
(4, 15000.90, '2023-03-05'),
(4, 41000.25, '2023-03-12'),
(4, 32000.60, '2023-03-19'),
(4, 28000.75, '2023-03-26'),

-- Église 5
(5, 27000.40, '2023-03-05'),
(5, 38000.65, '2023-03-12'),
(5, 45000.30, '2023-03-19'),
(5, 21000.75, '2023-03-26');

-- Avril 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-04-02'),
(1, 18000.50, '2023-04-09'),
(1, 32000.25, '2023-04-16'),
(1, 15000.80, '2023-04-23'),
(1, 41000.60, '2023-04-30'),

-- Église 2
(2, 38000.35, '2023-04-02'),
(2, 29000.45, '2023-04-09'),
(2, 48000.70, '2023-04-16'),
(2, 42000.25, '2023-04-23'),
(2, 20000.90, '2023-04-30'),

-- Église 3
(3, 42000.25, '2023-04-02'),
(3, 35000.80, '2023-04-09'),
(3, 29000.55, '2023-04-16'),
(3, 18000.70, '2023-04-23'),
(3, 47000.40, '2023-04-30'),

-- Église 4
(4, 15000.90, '2023-04-02'),
(4, 41000.25, '2023-04-09'),
(4, 32000.60, '2023-04-16'),
(4, 28000.75, '2023-04-23'),
(4, 39000.40, '2023-04-30'),

-- Église 5
(5, 27000.40, '2023-04-02'),
(5, 38000.65, '2023-04-09'),
(5, 45000.30, '2023-04-16'),
(5, 21000.75, '2023-04-23'),
(5, 32000.50, '2023-04-30');

-- Continuez de la même manière pour les autres mois

-- Mai 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-05-07'),
(1, 18000.50, '2023-05-14'),
(1, 32000.25, '2023-05-21'),
(1, 15000.80, '2023-05-28'),

-- Église 2
(2, 38000.35, '2023-05-07'),
(2, 29000.45, '2023-05-14'),
(2, 48000.70, '2023-05-21'),
(2, 42000.25, '2023-05-28'),

-- Église 3
(3, 42000.25, '2023-05-07'),
(3, 35000.80, '2023-05-14'),
(3, 29000.55, '2023-05-21'),
(3, 18000.70, '2023-05-28'),

-- Église 4
(4, 15000.90, '2023-05-07'),
(4, 41000.25, '2023-05-14'),
(4, 32000.60, '2023-05-21'),
(4, 28000.75, '2023-05-28'),

-- Église 5
(5, 27000.40, '2023-05-07'),
(5, 38000.65, '2023-05-14'),
(5, 45000.30, '2023-05-21'),
(5, 21000.75, '2023-05-28');

-- Juin 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-06-04'),
(1, 18000.50, '2023-06-11'),
(1, 32000.25, '2023-06-18'),
(1, 15000.80, '2023-06-25'),

-- Église 2
(2, 38000.35, '2023-06-04'),
(2, 29000.45, '2023-06-11'),
(2, 48000.70, '2023-06-18'),
(2, 42000.25, '2023-06-25'),

-- Église 3
(3, 42000.25, '2023-06-04'),
(3, 35000.80, '2023-06-11'),
(3, 29000.55, '2023-06-18'),
(3, 18000.70, '2023-06-25'),

-- Église 4
(4, 15000.90, '2023-06-04'),
(4, 41000.25, '2023-06-11'),
(4, 32000.60, '2023-06-18'),
(4, 28000.75, '2023-06-25'),

-- Église 5
(5, 27000.40, '2023-06-04'),
(5, 38000.65, '2023-06-11'),
(5, 45000.30, '2023-06-18'),
(5, 21000.75, '2023-06-25');

-- Continuez de la même manière pour les autres mois

-- Juillet 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-07-02'),
(1, 18000.50, '2023-07-09'),
(1, 32000.25, '2023-07-16'),
(1, 15000.80, '2023-07-23'),
(1, 41000.60, '2023-07-30'),

-- Église 2
(2, 38000.35, '2023-07-02'),
(2, 29000.45, '2023-07-09'),
(2, 48000.70, '2023-07-16'),
(2, 42000.25, '2023-07-23'),
(2, 20000.90, '2023-07-30'),

-- Église 3
(3, 42000.25, '2023-07-02'),
(3, 35000.80, '2023-07-09'),
(3, 29000.55, '2023-07-16'),
(3, 18000.70, '2023-07-23'),
(3, 47000.40, '2023-07-30'),

-- Église 4
(4, 15000.90, '2023-07-02'),
(4, 41000.25, '2023-07-09'),
(4, 32000.60, '2023-07-16'),
(4, 28000.75, '2023-07-23'),
(4, 39000.40, '2023-07-30'),

-- Église 5
(5, 27000.40, '2023-07-02'),
(5, 38000.65, '2023-07-09'),
(5, 45000.30, '2023-07-16'),
(5, 21000.75, '2023-07-23'),
(5, 32000.50, '2023-07-30');

-- Août 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-08-06'),
(1, 18000.50, '2023-08-13'),
(1, 32000.25, '2023-08-20'),
(1, 15000.80, '2023-08-27'),

-- Église 2
(2, 38000.35, '2023-08-06'),
(2, 29000.45, '2023-08-13'),
(2, 48000.70, '2023-08-20'),
(2, 42000.25, '2023-08-27'),

-- Église 3
(3, 42000.25, '2023-08-06'),
(3, 35000.80, '2023-08-13'),
(3, 29000.55, '2023-08-20'),
(3, 18000.70, '2023-08-27'),

-- Église 4
(4, 15000.90, '2023-08-06'),
(4, 41000.25, '2023-08-13'),
(4, 32000.60, '2023-08-20'),
(4, 28000.75, '2023-08-27'),

-- Église 5
(5, 27000.40, '2023-08-06'),
(5, 38000.65, '2023-08-13'),
(5, 45000.30, '2023-08-20'),
(5, 21000.75, '2023-08-27');

-- Continuez de la même manière pour les autres mois

-- Septembre 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-09-03'),
(1, 18000.50, '2023-09-10'),
(1, 32000.25, '2023-09-17'),
(1, 15000.80, '2023-09-24'),

-- Église 2
(2, 38000.35, '2023-09-03'),
(2, 29000.45, '2023-09-10'),
(2, 48000.70, '2023-09-17'),
(2, 42000.25, '2023-09-24'),

-- Église 3
(3, 42000.25, '2023-09-03'),
(3, 35000.80, '2023-09-10'),
(3, 29000.55, '2023-09-17'),
(3, 18000.70, '2023-09-24'),

-- Église 4
(4, 15000.90, '2023-09-03'),
(4, 41000.25, '2023-09-10'),
(4, 32000.60, '2023-09-17'),
(4, 28000.75, '2023-09-24'),

-- Église 5
(5, 27000.40, '2023-09-03'),
(5, 38000.65, '2023-09-10'),
(5, 45000.30, '2023-09-17'),
(5, 21000.75, '2023-09-24');

-- Octobre 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-10-01'),
(1, 18000.50, '2023-10-08'),
(1, 32000.25, '2023-10-15'),
(1, 15000.80, '2023-10-22'),
(1, 41000.60, '2023-10-29'),

-- Église 2
(2, 38000.35, '2023-10-01'),
(2, 29000.45, '2023-10-08'),
(2, 48000.70, '2023-10-15'),
(2, 42000.25, '2023-10-22'),
(2, 20000.90, '2023-10-29'),

-- Église 3
(3, 42000.25, '2023-10-01'),
(3, 35000.80, '2023-10-08'),
(3, 29000.55, '2023-10-15'),
(3, 18000.70, '2023-10-22'),
(3, 47000.40, '2023-10-29'),

-- Église 4
(4, 15000.90, '2023-10-01'),
(4, 41000.25, '2023-10-08'),
(4, 32000.60, '2023-10-15'),
(4, 28000.75, '2023-10-22'),
(4, 39000.40, '2023-10-29'),

-- Église 5
(5, 27000.40, '2023-10-01'),
(5, 38000.65, '2023-10-08'),
(5, 45000.30, '2023-10-15'),
(5, 21000.75, '2023-10-22'),
(5, 32000.50, '2023-10-29');

-- Continuez de la même manière pour les autres mois


-- Novembre 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-11-05'),
(1, 18000.50, '2023-11-12'),
(1, 32000.25, '2023-11-19'),
(1, 15000.80, '2023-11-26'),

-- Église 2
(2, 38000.35, '2023-11-05'),
(2, 29000.45, '2023-11-12'),
(2, 48000.70, '2023-11-19'),
(2, 42000.25, '2023-11-26'),

-- Église 3
(3, 42000.25, '2023-11-05'),
(3, 35000.80, '2023-11-12'),
(3, 29000.55, '2023-11-19'),
(3, 18000.70, '2023-11-26'),

-- Église 4
(4, 15000.90, '2023-11-05'),
(4, 41000.25, '2023-11-12'),
(4, 32000.60, '2023-11-19'),
(4, 28000.75, '2023-11-26'),

-- Église 5
(5, 27000.40, '2023-11-05'),
(5, 38000.65, '2023-11-12'),
(5, 45000.30, '2023-11-19'),
(5, 21000.75, '2023-11-26');

-- Décembre 2023
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2023-12-03'),
(1, 18000.50, '2023-12-10'),
(1, 32000.25, '2023-12-17'),
(1, 15000.80, '2023-12-24'),
(1, 41000.60, '2023-12-31'),

-- Église 2
(2, 38000.35, '2023-12-03'),
(2, 29000.45, '2023-12-10'),
(2, 48000.70, '2023-12-17'),
(2, 42000.25, '2023-12-24'),
(2, 20000.90, '2023-12-31'),

-- Église 3
(3, 42000.25, '2023-12-03'),
(3, 35000.80, '2023-12-10'),
(3, 29000.55, '2023-12-17'),
(3, 18000.70, '2023-12-24'),
(3, 47000.40, '2023-12-31'),

-- Église 4
(4, 15000.90, '2023-12-03'),
(4, 41000.25, '2023-12-10'),
(4, 32000.60, '2023-12-17'),
(4, 28000.75, '2023-12-24'),
(4, 39000.40, '2023-12-31'),

-- Église 5
(5, 27000.40, '2023-12-03'),
(5, 38000.65, '2023-12-10'),
(5, 45000.30, '2023-12-17'),
(5, 21000.75, '2023-12-24'),
(5, 32000.50, '2023-12-31');

-- Continuez de la même manière pour les autres mois


-- Janvier 2024
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2024-01-07'),
(1, 18000.50, '2024-01-14'),
(1, 32000.25, '2024-01-21'),
(1, 15000.80, '2024-01-28'),

-- Église 2
(2, 38000.35, '2024-01-07'),
(2, 29000.45, '2024-01-14'),
(2, 48000.70, '2024-01-21'),
(2, 42000.25, '2024-01-28'),

-- Église 3
(3, 42000.25, '2024-01-07'),
(3, 35000.80, '2024-01-14'),
(3, 29000.55, '2024-01-21'),
(3, 18000.70, '2024-01-28'),

-- Église 4
(4, 15000.90, '2024-01-07'),
(4, 41000.25, '2024-01-14'),
(4, 32000.60, '2024-01-21'),
(4, 28000.75, '2024-01-28'),

-- Église 5
(5, 27000.40, '2024-01-07'),
(5, 38000.65, '2024-01-14'),
(5, 45000.30, '2024-01-21'),
(5, 21000.75, '2024-01-28');

-- Février 2024
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 25000.75, '2024-02-04'),
(1, 18000.50, '2024-02-11'),
(1, 32000.25, '2024-02-18'),
(1, 15000.80, '2024-02-25'),

-- Église 2
(2, 38000.35, '2024-02-04'),
(2, 29000.45, '2024-02-11'),
(2, 48000.70, '2024-02-18'),
(2, 42000.25, '2024-02-25'),

-- Église 3
(3, 42000.25, '2024-02-04'),
(3, 35000.80, '2024-02-11'),
(3, 29000.55, '2024-02-18'),
(3, 18000.70, '2024-02-25'),

-- Église 4
(4, 15000.90, '2024-02-04'),
(4, 41000.25, '2024-02-11'),
(4, 32000.60, '2024-02-18'),
(4, 28000.75, '2024-02-25'),

-- Église 5
(5, 27000.40, '2024-02-04'),
(5, 38000.65, '2024-02-11'),
(5, 45000.30, '2024-02-18'),
(5, 21000.75, '2024-02-25');

-- Mars
INSERT INTO caisse (id_eglise, montant, datetime) VALUES
-- Église 1
(1, 20000.75, '2024-03-03'),
(1, 14000.50, '2024-03-10'),
(1, 33000.25, '2024-03-17'),
(1, 17000.80, '2024-03-24'),

-- Église 2
(2, 38000.35, '2024-03-03'),
(2, 29000.45, '2024-03-10'),
(2, 48000.70, '2024-03-17'),
(2, 42000.25, '2024-03-24'),

-- Église 3
(3, 42000.25, '2024-03-03'),
(3, 35000.80, '2024-03-10'),
(3, 29000.55, '2024-03-17'),
(3, 18000.70, '2024-03-24'),

-- Église 4
(4, 15000.90, '2024-03-03'),
(4, 41000.25, '2024-03-10'),
(4, 32000.60, '2024-03-17'),
(4, 28000.75, '2024-03-24'),

-- Église 5
(5, 22000.40, '2024-03-03'),
(5, 30000.65, '2024-03-10'),
(5, 47000.30, '2024-03-17'),
(5, 22000.75, '2024-03-24');