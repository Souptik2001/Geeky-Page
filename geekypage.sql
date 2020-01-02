-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2020 at 07:13 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `geekypage`
--

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `sl_no` int(50) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `ph_no` varchar(11) NOT NULL,
  `message` varchar(50) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`sl_no`, `name`, `email`, `ph_no`, `message`, `date`) VALUES
(1, 'Firstname', 'first@gmail.com', '1234567890', 'This is first manually generated post.', '2019-12-27 15:44:12'),
(2, 'Souptik Datta', 'souptikdatta2001@gma', '6565656565', 'Hello this is my message great blog page....Yo!!', '2019-12-27 15:58:51');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sl_no` int(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `body` varchar(100) NOT NULL,
  `wr_by` varchar(20) NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `slug` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sl_no`, `title`, `body`, `wr_by`, `date`, `slug`) VALUES
(1, 'First Post', 'This is the first post.', 'S.D', '2020-01-01 19:46:09', 'first-post'),
(3, 'Third post', 'Hello this is another new post made through the website itself', 'S.D', NULL, 'third-post'),
(4, 'Fourth Post', 'This is also a post through website but this time time will also be included', 'S.D', '2019-12-31 23:25:58', 'fourth-post'),
(5, 'Fifth Posttt', 'Hello changing it.......Changed it.', 'S.D', '2020-01-01 22:28:25', 'fifth-post');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`sl_no`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sl_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `sl_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sl_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
