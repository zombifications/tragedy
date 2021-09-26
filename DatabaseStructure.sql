CREATE DATABASE IF NOT EXISTS `tragedy`;
USE `tragedy`;

--
-- Table structure for table `prefix`
--

DROP TABLE IF EXISTS `prefix`;


CREATE TABLE `prefix` (
  `guild` varchar(18) DEFAULT NULL,
  `prefix1` varchar(10) DEFAULT NULL,
  `prefix2` varchar(10) DEFAULT NULL,
  `prefix3` varchar(10) DEFAULT NULL,
  `prefix4` varchar(10) DEFAULT NULL,
  `prefix5` varchar(10) DEFAULT NULL,
  `defaultPrefix` varchar(3) DEFAULT 'xv ',
  UNIQUE KEY `guild` (`guild`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `warns`
--

DROP TABLE IF EXISTS `warns`;


CREATE TABLE `warns` (
  `id` varchar(10) NOT NULL,
  `guild` varchar(19) NOT NULL,
  `user` varchar(18) NOT NULL,
  `warner` varchar(18) NOT NULL,
  `reason` varchar(125) NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `temp-emails`
--

DROP TABLE IF EXISTS `temp-emails`;


CREATE TABLE `temp-emails` (
  `user` varchar(18) NOT NULL,
  `email` varchar(255),
  UNIQUE KEY `user` (`user`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `welcome`
--

DROP TABLE IF EXISTS `welcome`;


CREATE TABLE `welcome` (
  `guild` varchar(18) NOT NULL,
  `channel` varchar(18) DEFAULT NULL,
  `message` varchar(1850) NULL DEFAULT 'Welcome user_ping to server_name !',
  UNIQUE KEY `guild` (`guild`),
  UNIQUE KEY `channel` (`channel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `economy`
--

DROP TABLE IF EXISTS `economy`;


CREATE TABLE `economy` (
  `guild` varchar(18) NOT NULL,
  `user` varchar(18) NOT NULL,
  `balance` INT NOT NULL DEFAULT 0,
  `items` JSON DEFAULT '{}'
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

--
-- Table structure for table `auto-mod`
--

DROP TABLE IF EXISTS `auto-mod`;


CREATE TABLE `auto-mod` (
  `guild` varchar(18) NOT NULL,
  `profanity_filter` boolean NOT NULL DEFAULT 0,
  `invite_filter` boolean NOT NULL DEFAULT 0,
  `mention_filter` boolean NOT NULL DEFAULT 0,
  `mention_length` INT NOT NULL DEFAULT 0,
  `spam_filter` boolean NOT NULL DEFAULT 0,
  UNIQUE KEY `guild` (`guild`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Structure for `anti-nuke`
--

DROP TABLE IF EXISTS `anti-nuke`;
DROP TABLE IF EXISTS `anti-nuke-whitelist`;


CREATE TABLE `anti-nuke` (
  `guild` varchar(18) NOT NULL,
  `punishment` INT NOT NULL DEFAULT 0,
  `self_bot` boolean NOT NULL DEFAULT 0,
  UNIQUE KEY `guild` (`guild`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `anti-nuke-whitelist` (
  `guild` varchar(18) NOT NULL,
  `id` BIGINT(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;