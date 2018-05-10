-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2018 at 01:35 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `society_mysqldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `acc_name` varchar(14) NOT NULL,
  `flat_id` int(11) NOT NULL,
  `acc_pass` varchar(15) NOT NULL,
  `owner_name` varchar(127) NOT NULL,
  `pending_dues` decimal(10,2) NOT NULL,
  `profile_img` mediumblob
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`acc_name`, `flat_id`, `acc_pass`, `owner_name`, `pending_dues`, `profile_img`) VALUES
('10110', 111, 'Hello', 'Vineet', '10500.00', ''),
('10120', 112, '', 'Ameya', '12500.00', ''),
('10210', 211, '', 'Aman', '15000.00', ''),
('10220', 212, '', 'Yash', '20000.00', '');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `resident_id` int(11) NOT NULL,
  `society_id` int(11) NOT NULL,
  `admin_pass` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Stand-in structure for view `admin_view`
-- (See below for the actual view)
--
CREATE TABLE `admin_view` (
`resident_id` int(11)
,`society_id` int(11)
,`flat_id` int(11)
,`account_name` varchar(14)
);

-- --------------------------------------------------------

--
-- Table structure for table `basic_maintenance_bill`
--

CREATE TABLE `basic_maintenance_bill` (
  `bill_num` int(11) NOT NULL,
  `flat_id` int(11) NOT NULL,
  `bill_date` date NOT NULL,
  `water_charges` decimal(8,2) NOT NULL,
  `property_tax` decimal(8,2) NOT NULL,
  `elec_charges` decimal(8,2) NOT NULL,
  `sinking_fund` decimal(8,2) NOT NULL,
  `parking_charges` decimal(8,2) NOT NULL,
  `noc` decimal(8,2) NOT NULL,
  `insurance` decimal(8,2) NOT NULL,
  `other` decimal(8,2) NOT NULL,
  `due_date` date NOT NULL,
  `down_doc` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `committee_member`
--

CREATE TABLE `committee_member` (
  `resident_id` int(11) NOT NULL,
  `wing_id` int(11) NOT NULL,
  `flat_no` int(11) NOT NULL,
  `post` varchar(31) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `documents`
--

CREATE TABLE `documents` (
  `doc_id` int(11) NOT NULL,
  `flat_id` int(11) NOT NULL,
  `doc_name` varchar(31) NOT NULL,
  `upload_date` date NOT NULL,
  `path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `facility`
--

CREATE TABLE `facility` (
  `society_id` int(11) NOT NULL,
  `facility_name` varchar(31) NOT NULL,
  `price_per_hour` decimal(10,2) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `facility`
--

INSERT INTO `facility` (`society_id`, `facility_name`, `price_per_hour`, `start_time`, `end_time`) VALUES
(1001, 'Car Parking', '35.00', '09:00:00', '21:00:00'),
(1001, 'Gym', '250.00', '08:00:00', '22:00:00'),
(1001, 'Swimming Pool', '25.00', '07:30:00', '19:00:00'),
(1001, 'Turf', '120.00', '10:00:00', '17:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `flat`
--

CREATE TABLE `flat` (
  `flat_id` int(11) NOT NULL,
  `wing_id` int(11) NOT NULL,
  `flat_num` int(11) NOT NULL,
  `facing` varchar(31) NOT NULL,
  `area` int(11) NOT NULL,
  `BHK` decimal(2,1) NOT NULL,
  `floor_no` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flat`
--

INSERT INTO `flat` (`flat_id`, `wing_id`, `flat_num`, `facing`, `area`, `BHK`, `floor_no`, `price`) VALUES
(111, 101, 1, 'Road', 10, '2.0', 1, '10000.00'),
(112, 101, 2, 'Road', 10, '2.0', 1, '9200.00'),
(113, 101, 3, 'Road', 8, '3.0', 2, '10500.00'),
(114, 101, 4, 'Road', 8, '2.0', 2, '8700.00'),
(115, 101, 5, 'Garden', 6, '3.0', 3, '13760.00'),
(116, 101, 6, 'Garden', 4, '3.0', 3, '9600.00'),
(117, 101, 7, 'Garden', 4, '2.0', 4, '11500.25'),
(118, 101, 8, 'Garden', 6, '4.0', 4, '12000.00'),
(211, 102, 1, 'Forest', 12, '3.0', 1, '10090.00'),
(212, 102, 2, 'Road', 11, '3.5', 1, '10923.00'),
(213, 102, 3, 'Forest', 8, '2.5', 2, '7094.00'),
(214, 102, 4, 'Road', 9, '3.0', 2, '8044.00'),
(215, 102, 5, 'Forest', 12, '4.0', 3, '12000.00'),
(216, 102, 6, 'Road', 9, '2.0', 3, '9755.00'),
(217, 102, 7, 'Forest', 3, '1.0', 4, '5322.00'),
(218, 102, 8, 'Road', 10, '2.0', 4, '14000.00'),
(219, 102, 9, 'Forest', 6, '3.0', 5, '12746.00'),
(220, 102, 10, 'Road', 8, '2.0', 5, '13000.00');

-- --------------------------------------------------------

--
-- Stand-in structure for view `flat_addr`
-- (See below for the actual view)
--
CREATE TABLE `flat_addr` (
`flat_id` int(11)
,`wing_id` int(11)
,`society_id` int(11)
,`notice_id` int(11)
);

-- --------------------------------------------------------

--
-- Table structure for table `issues`
--

CREATE TABLE `issues` (
  `issue_id` int(11) NOT NULL,
  `acc_name` varchar(14) NOT NULL,
  `issue_date` date NOT NULL,
  `issue_desc` varchar(255) NOT NULL,
  `reported_by` varchar(127) NOT NULL,
  `related` varchar(31) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `issues`
--

INSERT INTO `issues` (`issue_id`, `acc_name`, `issue_date`, `issue_desc`, `reported_by`, `related`) VALUES
(1, '10110', '2018-04-12', 'Hello World Test! Until now, it refused to allow insertion of new issues', '', 'None'),
(2, '10110', '2018-04-12', 'Hello', '', 'Stationary'),
(3, '10110', '2018-04-12', 'Hello', '', 'Stationary'),
(4, '10120', '2018-04-12', 'The logout did not work for the previous account', '', 'Stationary'),
(5, '10120', '2018-04-12', 'Trying another logout', '', 'Stationary'),
(6, '10120', '2018-04-12', 'Why couldn\'t this have worked earlier?', '', 'Stationary');

-- --------------------------------------------------------

--
-- Stand-in structure for view `maintenance_bill`
-- (See below for the actual view)
--
CREATE TABLE `maintenance_bill` (
`bill_num` int(11)
,`flat_id` int(11)
,`bill_date` date
,`water_charges` decimal(8,2)
,`property_tax` decimal(8,2)
,`elec_charges` decimal(8,2)
,`sinking_fund` decimal(8,2)
,`parking_charges` decimal(8,2)
,`noc` decimal(8,2)
,`insurance` decimal(8,2)
,`other` decimal(8,2)
,`due_date` date
,`amount` decimal(15,2)
,`down_doc` varchar(255)
);

-- --------------------------------------------------------

--
-- Table structure for table `notices`
--

CREATE TABLE `notices` (
  `notice_id` int(11) NOT NULL,
  `society_id` int(11) NOT NULL,
  `notice_header` varchar(63) NOT NULL,
  `notice_date` date NOT NULL,
  `notice_desc` varchar(1023) NOT NULL,
  `valid_for_all_buildings` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `notices`
--

INSERT INTO `notices` (`notice_id`, `society_id`, `notice_header`, `notice_date`, `notice_desc`, `valid_for_all_buildings`) VALUES
(1111, 1001, 'Hello User!', '2018-04-11', 'This notice is a welcome notice for users', 1),
(1112, 1001, 'Water supply reduction for summer', '2018-04-08', 'Unfortunately, there have been a few water cuts over the years', 0),
(1113, 1001, 'Hello World', '2018-03-01', 'A message from the computer itself', 1);

-- --------------------------------------------------------

--
-- Table structure for table `resident`
--

CREATE TABLE `resident` (
  `resident_id` int(11) NOT NULL,
  `flat_id` int(11) NOT NULL,
  `resident_name` varchar(127) NOT NULL,
  `contact` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `resident`
--

INSERT INTO `resident` (`resident_id`, `flat_id`, `resident_name`, `contact`) VALUES
(11, 111, 'Vineet', 0),
(12, 112, 'Ameya', 0),
(13, 211, 'Aman', 0),
(14, 212, 'Yash', 0),
(15, 111, 'Rishabh', 0),
(16, 211, 'Jainam', 0),
(17, 111, 'A', 321),
(18, 112, 'A', 1234);

-- --------------------------------------------------------

--
-- Table structure for table `society`
--

CREATE TABLE `society` (
  `society_id` int(11) NOT NULL,
  `society_name` varchar(255) NOT NULL,
  `region` varchar(127) NOT NULL,
  `city` varchar(127) NOT NULL,
  `state` varchar(127) NOT NULL,
  `area` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `society`
--

INSERT INTO `society` (`society_id`, `society_name`, `region`, `city`, `state`, `area`) VALUES
(1001, 'VJTI Society', 'Matunga', 'Mumbai', 'Maharashtra', 10000);

-- --------------------------------------------------------

--
-- Table structure for table `wing`
--

CREATE TABLE `wing` (
  `wing_id` int(11) NOT NULL,
  `society_id` int(11) NOT NULL,
  `wing_name` varchar(15) NOT NULL,
  `no_of_floors` int(11) NOT NULL,
  `total_area` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `wing`
--

INSERT INTO `wing` (`wing_id`, `society_id`, `wing_name`, `no_of_floors`, `total_area`) VALUES
(101, 1001, 'Wing-A', 4, 100),
(102, 1001, 'Wing-B', 5, 125);

-- --------------------------------------------------------

--
-- Structure for view `admin_view`
--
DROP TABLE IF EXISTS `admin_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `admin_view`  AS  select `admin`.`resident_id` AS `resident_id`,`admin`.`society_id` AS `society_id`,`committee_member`.`flat_no` AS `flat_id`,`account`.`acc_name` AS `account_name` from ((`admin` left join `committee_member` on((`admin`.`resident_id` = `committee_member`.`resident_id`))) left join `account` on((`committee_member`.`flat_no` = `account`.`flat_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `flat_addr`
--
DROP TABLE IF EXISTS `flat_addr`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `flat_addr`  AS  select `flat`.`flat_id` AS `flat_id`,`wing`.`wing_id` AS `wing_id`,`wing`.`society_id` AS `society_id`,`notices`.`notice_id` AS `notice_id` from ((`flat` join `wing` on((`flat`.`wing_id` = `wing`.`wing_id`))) join `notices` on((`wing`.`society_id` = `notices`.`society_id`))) ;

-- --------------------------------------------------------

--
-- Structure for view `maintenance_bill`
--
DROP TABLE IF EXISTS `maintenance_bill`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `maintenance_bill`  AS  select `basic_maintenance_bill`.`bill_num` AS `bill_num`,`basic_maintenance_bill`.`flat_id` AS `flat_id`,`basic_maintenance_bill`.`bill_date` AS `bill_date`,`basic_maintenance_bill`.`water_charges` AS `water_charges`,`basic_maintenance_bill`.`property_tax` AS `property_tax`,`basic_maintenance_bill`.`elec_charges` AS `elec_charges`,`basic_maintenance_bill`.`sinking_fund` AS `sinking_fund`,`basic_maintenance_bill`.`parking_charges` AS `parking_charges`,`basic_maintenance_bill`.`noc` AS `noc`,`basic_maintenance_bill`.`insurance` AS `insurance`,`basic_maintenance_bill`.`other` AS `other`,`basic_maintenance_bill`.`due_date` AS `due_date`,(((((((`basic_maintenance_bill`.`water_charges` + `basic_maintenance_bill`.`property_tax`) + `basic_maintenance_bill`.`elec_charges`) + `basic_maintenance_bill`.`sinking_fund`) + `basic_maintenance_bill`.`parking_charges`) + `basic_maintenance_bill`.`noc`) + `basic_maintenance_bill`.`insurance`) + `basic_maintenance_bill`.`other`) AS `amount`,`basic_maintenance_bill`.`down_doc` AS `down_doc` from `basic_maintenance_bill` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`acc_name`),
  ADD KEY `flat_acc` (`flat_id`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `society_admin` (`society_id`);

--
-- Indexes for table `basic_maintenance_bill`
--
ALTER TABLE `basic_maintenance_bill`
  ADD PRIMARY KEY (`bill_num`),
  ADD KEY `flat_bill` (`flat_id`);

--
-- Indexes for table `committee_member`
--
ALTER TABLE `committee_member`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `wing_committee` (`wing_id`);

--
-- Indexes for table `documents`
--
ALTER TABLE `documents`
  ADD PRIMARY KEY (`doc_id`),
  ADD KEY `flat_docs` (`flat_id`);

--
-- Indexes for table `facility`
--
ALTER TABLE `facility`
  ADD PRIMARY KEY (`society_id`,`facility_name`);

--
-- Indexes for table `flat`
--
ALTER TABLE `flat`
  ADD PRIMARY KEY (`flat_id`),
  ADD KEY `wing_flat` (`wing_id`);

--
-- Indexes for table `issues`
--
ALTER TABLE `issues`
  ADD PRIMARY KEY (`issue_id`),
  ADD KEY `acc_issues` (`acc_name`);

--
-- Indexes for table `notices`
--
ALTER TABLE `notices`
  ADD PRIMARY KEY (`notice_id`),
  ADD KEY `society_notice` (`society_id`);

--
-- Indexes for table `resident`
--
ALTER TABLE `resident`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `flat_resident` (`flat_id`);

--
-- Indexes for table `society`
--
ALTER TABLE `society`
  ADD PRIMARY KEY (`society_id`),
  ADD KEY `society_id` (`society_id`);

--
-- Indexes for table `wing`
--
ALTER TABLE `wing`
  ADD PRIMARY KEY (`wing_id`),
  ADD KEY `society_wing` (`society_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `flat_acc` FOREIGN KEY (`flat_id`) REFERENCES `flat` (`flat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `member_admin` FOREIGN KEY (`resident_id`) REFERENCES `committee_member` (`resident_id`),
  ADD CONSTRAINT `society_admin` FOREIGN KEY (`society_id`) REFERENCES `society` (`society_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `basic_maintenance_bill`
--
ALTER TABLE `basic_maintenance_bill`
  ADD CONSTRAINT `flat_bill` FOREIGN KEY (`flat_id`) REFERENCES `flat` (`flat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `committee_member`
--
ALTER TABLE `committee_member`
  ADD CONSTRAINT `resident_member` FOREIGN KEY (`resident_id`) REFERENCES `resident` (`resident_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `wing_committee` FOREIGN KEY (`wing_id`) REFERENCES `wing` (`wing_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `documents`
--
ALTER TABLE `documents`
  ADD CONSTRAINT `flat_docs` FOREIGN KEY (`flat_id`) REFERENCES `flat` (`flat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `facility`
--
ALTER TABLE `facility`
  ADD CONSTRAINT `society_facility` FOREIGN KEY (`society_id`) REFERENCES `society` (`society_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `flat`
--
ALTER TABLE `flat`
  ADD CONSTRAINT `wing_flat` FOREIGN KEY (`wing_id`) REFERENCES `wing` (`wing_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `issues`
--
ALTER TABLE `issues`
  ADD CONSTRAINT `acc_issues` FOREIGN KEY (`acc_name`) REFERENCES `account` (`acc_name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `notices`
--
ALTER TABLE `notices`
  ADD CONSTRAINT `society_notice` FOREIGN KEY (`society_id`) REFERENCES `society` (`society_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `resident`
--
ALTER TABLE `resident`
  ADD CONSTRAINT `flat_resident` FOREIGN KEY (`flat_id`) REFERENCES `flat` (`flat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `wing`
--
ALTER TABLE `wing`
  ADD CONSTRAINT `society_wing` FOREIGN KEY (`society_id`) REFERENCES `society` (`society_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
