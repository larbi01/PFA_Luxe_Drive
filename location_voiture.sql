-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 05 mai 2023 à 19:17
-- Version du serveur : 10.4.24-MariaDB
-- Version de PHP : 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `location_voiture`
--

-- --------------------------------------------------------

--
-- Structure de la table `car`
--

CREATE TABLE `car` (
  `id_car` int(11) NOT NULL,
  `marque` varchar(40) NOT NULL,
  `model` varchar(5) NOT NULL,
  `type_carburant` varchar(20) NOT NULL,
  `nombre_place` varchar(2) NOT NULL,
  `transmission` varchar(20) NOT NULL,
  `prix_location` varchar(6) NOT NULL,
  `disponibilite` tinyint(1) NOT NULL DEFAULT 1,
  `matricule` varchar(20) NOT NULL,
  `car_image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `car`
--

INSERT INTO `car` (`id_car`, `marque`, `model`, `type_carburant`, `nombre_place`, `transmission`, `prix_location`, `disponibilite`, `matricule`, `car_image`) VALUES
(19, 'Bently Ghost', '2022', 'Essance', '4', 'Automatic', '2000', 1, '11111 B 11', 'bently.png'),
(20, 'Audi A7', '2021', 'Essance', '4', 'Manuel', '1500', 1, '25442 B 26', 'audi.jpg'),
(21, 'Lamborgini Verron', '2023', 'Essance', '2', 'Automatic', '2500', 1, '55555 B 23', 'black_lambo.png'),
(22, 'Audi Sport', '2023', 'Essance', '2', 'Automatic', '2700', 1, '25442 B 26', 'red_audi.png'),
(23, 'Mercedes G-Wagon', '2021', 'Gasoil', '4', 'Manuel', '1800', 1, '99999 B 26', 'mercedes_wagon.png'),
(24, 'Lamborgini Verron', '2022', 'Essance', '2', 'Automatic', '1800', 1, '25442 B 26', 'yellow_lambo.png'),
(25, 'Mercedes Class', '2022', 'Gasoil', '2', 'Automatic', '2000', 1, '22222 B 22', 'mercedes_black.png'),
(26, 'Ferrari G7', '2023', 'Essance', '2', 'Automatic', '2500', 1, '11111 B 11', 'red_ferari.png'),
(27, 'BMW X8', '2022', 'Gasoil', '4', 'Manuel', '1800', 1, '22222 B 22', 'bmw.png'),
(29, 'Porshe Panamera', '2021', 'Gasoil', '2', 'Manuel', '1500', 1, '77777 A 77', 'white_porshe.png');

-- --------------------------------------------------------

--
-- Structure de la table `contrat`
--

CREATE TABLE `contrat` (
  `id_paiment` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `finish_date` date NOT NULL,
  `mail` varchar(30) NOT NULL,
  `adresse` varchar(50) NOT NULL,
  `pays` varchar(30) NOT NULL,
  `ville` varchar(30) NOT NULL,
  `zip` int(7) NOT NULL,
  `rental_charge` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `contrat`
--

INSERT INTO `contrat` (`id_paiment`, `nom`, `prenom`, `start_date`, `finish_date`, `mail`, `adresse`, `pays`, `ville`, `zip`, `rental_charge`) VALUES
(64, 'OUADEIH', 'Larbi', '2023-05-06', '2023-05-23', 'smaiiil@gmail.com', 'RES ALAOUI IMM A LOT BOUIZGARNE', 'maroc', 'MARRAKECH', 40010, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `login`
--

CREATE TABLE `login` (
  `id_login` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `login`
--

INSERT INTO `login` (`id_login`, `username`, `mail`, `password`) VALUES
(13, 'admin', 'admin@admin.com', 'admin'),
(17, 'lar008', 'lar@gmail.com', 'sdfsdf'),
(18, 'fss', 'sdf@gmail.com', 'sdfsdf');

-- --------------------------------------------------------

--
-- Structure de la table `payment`
--

CREATE TABLE `payment` (
  `id` int(11) NOT NULL,
  `nom_carte` varchar(50) NOT NULL,
  `numero_carte` varchar(16) NOT NULL,
  `expiration` date NOT NULL,
  `cvv` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id_car`);

--
-- Index pour la table `contrat`
--
ALTER TABLE `contrat`
  ADD PRIMARY KEY (`id_paiment`);

--
-- Index pour la table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id_login`);

--
-- Index pour la table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `car`
--
ALTER TABLE `car`
  MODIFY `id_car` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `contrat`
--
ALTER TABLE `contrat`
  MODIFY `id_paiment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT pour la table `login`
--
ALTER TABLE `login`
  MODIFY `id_login` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT pour la table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
