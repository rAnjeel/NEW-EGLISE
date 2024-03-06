CREATE TABLE eglise (
    id INT PRIMARY KEY IDENTITY,
    nom VARCHAR(255) NOT NULL,
    argent FLOAT NOT NULL
);

CREATE TABLE croyant (
    id INT PRIMARY KEY IDENTITY,
    nom VARCHAR(255) NOT NULL,
    
    id_eglise INT,
    login VARCHAR(255) NOT NULL,
    mdp VARCHAR(255) NOT NULL,
    statut VARCHAR(10) CONSTRAINT DF_Croyant_Statut DEFAULT 'pasteur' CHECK (statut IN ('croyant', 'pasteur')),
    CONSTRAINT FK_croyant_eglise FOREIGN KEY (id_eglise) REFERENCES eglise(id)
);

CREATE TABLE caisse (
    id INT PRIMARY KEY IDENTITY,
    id_eglise INT,
    montant FLOAT NOT NULL,
    datetime DATE NOT NULL,
    CONSTRAINT FK_caisse_eglise FOREIGN KEY (id_eglise) REFERENCES eglise(id)
);

CREATE TABLE estimation (
    id INT PRIMARY KEY IDENTITY,
    id_eglise INT,
    montant FLOAT NOT NULL,
    dimanche DATE NOT NULL,
    CONSTRAINT FK_estimation_eglise FOREIGN KEY (id_eglise) REFERENCES eglise(id)
);

CREATE TABLE pret (
    id INT PRIMARY KEY IDENTITY,
    id_croyant INT,
    montant FLOAT NOT NULL,
    dateDemande DATE NOT NULL,
    dateObtention DATE,
    CONSTRAINT FK_pret_croyant FOREIGN KEY (id_croyant) REFERENCES croyant(id)
);

CREATE TABLE situation (
    id_situation INT PRIMARY KEY IDENTITY,
    id_croyant INT,
    matrimoniale VARCHAR(300) NOT NULL DEFAULT 'celibataire' CHECK (matrimoniale IN ('celibataire', 'marie(e)', 'divorce(e)')),
    bapteme DATE,
    communion DATE,
    CONSTRAINT FK_situation_croyant FOREIGN KEY (id_croyant) REFERENCES croyant(id)
);

CREATE TABLE prediction_eglise (
    id INT PRIMARY KEY IDENTITY,
    id_eglise INT,
    reste FLOAT NOT NULL,
    dateDemande DATE NOT NULL,
    dateObtention DATE,
    CONSTRAINT FK_prediction_eglise FOREIGN KEY (id_eglise) REFERENCES eglise(id)
);
