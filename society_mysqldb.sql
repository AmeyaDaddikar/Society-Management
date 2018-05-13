-- phpMyAdmin SQL Dump
-- version 4.7.7
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2018 at 07:42 PM
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
  `profile_img` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`acc_name`, `flat_id`, `acc_pass`, `owner_name`, `pending_dues`, `profile_img`) VALUES
('CresTow31', 5, 'AccPass', 'A', '198.20', ''),
('CresTow32', 10, 'AccPass', 'A', '990.15', ''),
('CresTow33', 15, 'AccPass', 'A', '850.43', ''),
('CresTow34', 20, 'AccPass', 'A', '661.53', ''),
('CresTow41', 1, 'Pass', 'Nakula Dalavi', '0.00', ''),
('CresTow42', 6, 'AccPass', 'A', '521.89', ''),
('CresTow43', 11, 'AccPass', 'A', '551.49', ''),
('CresTow44', 16, 'AccPass', 'A', '472.07', ''),
('CresTow61', 4, 'AccPass', 'A', '878.41', ''),
('CresTow62', 9, 'AccPass', 'A', '919.58', ''),
('CresTow63', 14, 'AccPass', 'A', '374.03', ''),
('CresTow64', 19, 'AccPass', 'A', '688.46', ''),
('CresUC21', 2, 'AccPass', 'A', '817.15', ''),
('CresUC22', 7, 'AccPass', 'A', '588.88', ''),
('CresUC23', 12, 'AccPass', 'A', '616.93', ''),
('CresUC24', 17, 'AccPass', 'A', '547.69', ''),
('CresUC31', 3, 'AccPass', 'A', '713.66', ''),
('CresUC32', 8, 'AccPass', 'A', '735.00', ''),
('CresUC33', 13, 'AccPass', 'A', '409.18', ''),
('CresUC34', 18, 'AccPass', 'A', '777.76', '');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `acc_name` varchar(15) NOT NULL,
  `resident_id` int(11) NOT NULL,
  `society_id` int(11) NOT NULL,
  `admin_pass` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`acc_name`, `resident_id`, `society_id`, `admin_pass`) VALUES
('CresAdmin1', 7, 1, 'AdminPass');

-- --------------------------------------------------------

--
-- Stand-in structure for view `admin_flat`
-- (See below for the actual view)
--
CREATE TABLE `admin_flat` (
`acc_name` varchar(15)
,`flat_id` int(11)
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
  `post` varchar(31) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `committee_member`
--

INSERT INTO `committee_member` (`resident_id`, `wing_id`, `post`) VALUES
(1, 1, 'Treasurer'),
(6, 3, 'Chairman'),
(7, 3, 'Admin');

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
(1, 'Car parking', '25.00', '00:00:00', '00:00:00'),
(1, 'Gym', '150.00', '05:00:00', '22:00:00'),
(1, 'Swimming Pool', '50.00', '06:00:00', '19:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `flat`
--

CREATE TABLE `flat` (
  `flat_id` int(11) NOT NULL,
  `wing_id` int(11) NOT NULL,
  `flat_num` int(11) NOT NULL,
  `facing` varchar(31) NOT NULL,
  `area` decimal(6,2) NOT NULL,
  `BHK` decimal(2,1) NOT NULL,
  `floor_no` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flat`
--

INSERT INTO `flat` (`flat_id`, `wing_id`, `flat_num`, `facing`, `area`, `BHK`, `floor_no`, `price`) VALUES
(1, 1, 1, 'Road', '122.63', '2.0', 1, '14901257.36'),
(2, 2, 1, 'Garden', '183.08', '3.0', 1, '7264300.33'),
(3, 3, 1, 'Road', '165.98', '3.0', 1, '14679345.69'),
(4, 4, 1, 'Road', '128.28', '4.0', 1, '6898278.36'),
(5, 5, 1, 'Garden', '171.15', '2.0', 1, '13927108.77'),
(6, 1, 2, 'Garden', '164.51', '3.0', 1, '5994075.69'),
(7, 2, 2, 'Road', '145.26', '2.0', 1, '5266672.67'),
(8, 3, 2, 'Garden', '193.56', '2.0', 1, '14847875.91'),
(9, 4, 2, 'Garden', '188.87', '3.0', 1, '6313682.72'),
(10, 5, 2, 'Road', '197.78', '4.0', 1, '7061944.77'),
(11, 1, 3, 'Road', '113.44', '3.0', 2, '14199216.33'),
(12, 2, 3, 'Garden', '113.13', '2.0', 2, '10231816.58'),
(13, 3, 3, 'Road', '153.73', '3.0', 2, '13852142.43'),
(14, 4, 3, 'Road', '119.42', '2.0', 2, '13149057.86'),
(15, 5, 3, 'Garden', '126.67', '3.0', 2, '6575387.59'),
(16, 1, 4, 'Garden', '182.47', '2.0', 2, '5920659.02'),
(17, 2, 4, 'Road', '164.05', '2.0', 2, '14690337.61'),
(18, 3, 4, 'Garden', '174.44', '2.0', 2, '13791953.26'),
(19, 4, 4, 'Garden', '161.26', '2.0', 2, '14819224.63'),
(20, 5, 4, 'Road', '126.96', '2.0', 2, '11881943.88');

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
(1, 'CresTow41', '2018-05-13', 'The pool had a strange smell', '', 'Pool Facilities');

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
  `notice_desc` varchar(1023) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `notices`
--

INSERT INTO `notices` (`notice_id`, `society_id`, `notice_header`, `notice_date`, `notice_desc`) VALUES
(1, 1, 'Welcome notice', '2017-09-12', 'Welcome to all the new members! An orientation will be held in the society hall on 21/09/2017. At least one member of each flat is required to attend it, however, all are welcome.\r\n\r\nThe Secretary,\r\nCrescent Bay'),
(2, 1, 'Proposal for Day Care Centre', '2017-11-08', 'There has been made a proposal, numbered PR-DCC-001, for a day care centre next to the society park. The proposal has been sent to the members by email. Please review it before the next vote.\r\n\r\nThe Secretary,\r\nCrescent Bay');

-- --------------------------------------------------------

--
-- Table structure for table `notice_wing`
--

CREATE TABLE `notice_wing` (
  `notice_id` int(11) NOT NULL,
  `wing_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `resident`
--

CREATE TABLE `resident` (
  `resident_id` int(11) NOT NULL,
  `flat_id` int(11) NOT NULL,
  `resident_name` varchar(127) NOT NULL,
  `contact` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `resident`
--

INSERT INTO `resident` (`resident_id`, `flat_id`, `resident_name`, `contact`) VALUES
(1, 1, 'Nakula Dalavi ', '91'),
(2, 3, 'Sooraj Satavelekar ', '91'),
(3, 1, 'Nasatya Barvadekar ', '74'),
(4, 2, 'Ishwar Randhawa ', '528'),
(5, 2, 'Sayana Sinha ', '91'),
(6, 3, 'Har Kanungo ', '91'),
(7, 3, 'Sarasvati Ojha ', '68'),
(8, 4, 'Jaya Roychaudhuri ', '60'),
(9, 4, 'Madri Upandhye ', '601'),
(10, 2, 'Sarama Divekar ', '91');

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
  `area` decimal(5,2) NOT NULL COMMENT 'in acres'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `society`
--

INSERT INTO `society` (`society_id`, `society_name`, `region`, `city`, `state`, `area`) VALUES
(1, 'Crescent Bay', 'Parel, South Mumbai', 'Mumbai', 'Maharashtra', '5.48');

-- --------------------------------------------------------

--
-- Table structure for table `wing`
--

CREATE TABLE `wing` (
  `wing_id` int(11) NOT NULL,
  `society_id` int(11) NOT NULL,
  `wing_name` varchar(15) NOT NULL,
  `no_of_floors` int(11) NOT NULL,
  `total_area` decimal(6,4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `wing`
--

INSERT INTO `wing` (`wing_id`, `society_id`, `wing_name`, `no_of_floors`, `total_area`) VALUES
(1, 1, 'Tower 4', 45, '1.0467'),
(2, 1, 'UC2', 53, '1.2340'),
(3, 1, 'UC3', 37, '0.8900'),
(4, 1, 'Tower 6', 21, '0.5410'),
(5, 1, 'Tower 3', 59, '1.7300');

-- --------------------------------------------------------

--
-- Structure for view `admin_flat`
--
DROP TABLE IF EXISTS `admin_flat`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `admin_flat`  AS  select `admin`.`acc_name` AS `acc_name`,`resident`.`flat_id` AS `flat_id` from (((`admin` join `committee_member` on((`admin`.`resident_id` = `committee_member`.`resident_id`))) join `resident` on((`admin`.`resident_id` = `resident`.`resident_id`))) join `flat` on((`resident`.`flat_id` = `flat`.`flat_id`))) ;

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
  ADD PRIMARY KEY (`resident_id`);

--
-- Indexes for table `basic_maintenance_bill`
--
ALTER TABLE `basic_maintenance_bill`
  ADD PRIMARY KEY (`bill_num`),
  ADD UNIQUE KEY `bill_date` (`bill_date`),
  ADD KEY `flat_bill` (`flat_id`);

--
-- Indexes for table `committee_member`
--
ALTER TABLE `committee_member`
  ADD PRIMARY KEY (`resident_id`),
  ADD KEY `wing_member` (`wing_id`);

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
-- Indexes for table `notice_wing`
--
ALTER TABLE `notice_wing`
  ADD KEY `notice_constraint` (`notice_id`),
  ADD KEY `wing_notice` (`wing_id`);

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
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `basic_maintenance_bill`
--
ALTER TABLE `basic_maintenance_bill`
  MODIFY `bill_num` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `documents`
--
ALTER TABLE `documents`
  MODIFY `doc_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `flat`
--
ALTER TABLE `flat`
  MODIFY `flat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `issues`
--
ALTER TABLE `issues`
  MODIFY `issue_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `notices`
--
ALTER TABLE `notices`
  MODIFY `notice_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `resident`
--
ALTER TABLE `resident`
  MODIFY `resident_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `society`
--
ALTER TABLE `society`
  MODIFY `society_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `wing`
--
ALTER TABLE `wing`
  MODIFY `wing_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `flat_acc` FOREIGN KEY (`flat_id`) REFERENCES `flat` (`flat_id`) ON DELETE CASCADE ON UPDATE CASCADE;

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
  ADD CONSTRAINT `wing_member` FOREIGN KEY (`wing_id`) REFERENCES `wing` (`wing_id`) ON DELETE CASCADE ON UPDATE CASCADE;

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
-- Constraints for table `notice_wing`
--
ALTER TABLE `notice_wing`
  ADD CONSTRAINT `notice_constraint` FOREIGN KEY (`notice_id`) REFERENCES `notices` (`notice_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `wing_notice` FOREIGN KEY (`wing_id`) REFERENCES `wing` (`wing_id`) ON DELETE CASCADE ON UPDATE CASCADE;

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
