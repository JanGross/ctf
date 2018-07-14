-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema ctf_main
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ctf_main` ;

-- -----------------------------------------------------
-- Schema ctf_main
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ctf_main` DEFAULT CHARACTER SET utf8 ;
USE `ctf_main` ;

-- -----------------------------------------------------
-- Table `ctf_main`.`challenge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ctf_main`.`challenge` (
  `challenge_id` INT NOT NULL,
  `challenge_name` VARCHAR(45) NOT NULL,
  `challenge_description` VARCHAR(45) NULL,
  `challenge_flag` VARCHAR(45) NOT NULL,
  `challenge_score` INT NOT NULL,
  PRIMARY KEY (`challenge_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ctf_main`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ctf_main`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(160) NOT NULL,
  `active` TINYINT NOT NULL DEFAULT 1,
  `registered` DATETIME NULL DEFAULT NOW(),
  `info` VARCHAR(500) NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ctf_main`.`solved_challenges`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ctf_main`.`solved_challenges` (
  `user_id` INT NOT NULL,
  `challenge_id` INT NOT NULL,
  `submission_timestamp` DATETIME NOT NULL,
  PRIMARY KEY (`user_id`),
  INDEX `fk_challenge_id_idx` (`challenge_id` ASC),
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `ctf_main`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_challenge_id`
    FOREIGN KEY (`challenge_id`)
    REFERENCES `ctf_main`.`challenge` (`challenge_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
