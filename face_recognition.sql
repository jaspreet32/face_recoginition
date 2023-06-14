-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 29, 2021 at 07:25 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendence`
--

CREATE TABLE `attendence` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `roll_no` varchar(250) NOT NULL,
  `department` varchar(250) NOT NULL,
  `login_datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(250) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `book` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendence`
--

INSERT INTO `attendence` (`id`, `name`, `roll_no`, `department`, `login_datetime`, `status`, `semester`, `book`, `author`) VALUES
(202, 'Ashita', '1209', 'Electronics', '2021-06-29 04:20:11', 'checkin', '', '', ''),
(203, 'Ashita', '1209', 'Electronics', '2021-06-29 04:20:57', 'checkout', '2', 'Maths-2', '{upasana publisher}');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `department` varchar(45) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`id`, `semester`, `department`, `book_name`, `author`) VALUES
(1, 1, 'Computer Science', 'Maths-1', 'eagle'),
(2, 1, 'Computer Science', 'English-1', 'rd sharma'),
(3, 2, 'Electronics', 'Maths-2', 'upasana publisher'),
(4, 2, 'Electronics', 'English-2', 'evergreen'),
(5, 3, 'Computer Science', 'DE', 'arora books'),
(6, 3, 'Computer Science', 'OS', 'pubishers jagdamba'),
(11, 3, 'Electronics', 'RDBMS', 'Ishaan Publishers');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `username`, `email`, `password`) VALUES
(81, 'ashita', 'NULL', 'ashitagupta');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `username`, `email`, `password`) VALUES
(40, 'ashita', 'ashitagupta09@gmail.com', 'ashitagupta');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `department` varchar(45) NOT NULL,
  `course` varchar(45) NOT NULL,
  `year` varchar(45) NOT NULL,
  `semester` varchar(45) NOT NULL,
  `student_id` int(45) NOT NULL,
  `student_name` varchar(45) NOT NULL,
  `division` varchar(45) NOT NULL,
  `roll_no` varchar(45) NOT NULL,
  `gender` varchar(45) NOT NULL,
  `dob` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `teacher` varchar(45) NOT NULL,
  `photo_sample` varchar(45) NOT NULL,
  `status` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`department`, `course`, `year`, `semester`, `student_id`, `student_name`, `division`, `roll_no`, `gender`, `dob`, `email`, `phone`, `address`, `teacher`, `photo_sample`, `status`) VALUES
('Electronics', 'RDBMS', '2021-2022', '3', 13, 'Ashita', 'L', '1209', 'Female', '04/17/2002', 'ashita@gamil.com', '98154388114', '1443 phase 2', 'mam', 'Yes', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendence`
--
ALTER TABLE `attendence`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendence`
--
ALTER TABLE `attendence`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=204;

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(45) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
