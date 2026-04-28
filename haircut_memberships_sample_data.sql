INSERT INTO customer 
(cfirst_name, clast_name, membership_status, phone_number, email, username, password, address, city, state)
VALUES
('John', 'Doe', 1, '7045551234', 'john@example.com', 'jdoe', 'pass123', '123 Main St', 'Charlotte', 'NC'),
('Jane', 'Smith', 0, '7045555678', 'jane@example.com', 'jsmith', 'pass123', '456 Oak Ave', 'Gastonia', 'NC'),
('Mike', 'Brown', 1, '7045559999', 'mike@example.com', 'mbrown', 'pass123', '789 Pine Rd', 'Belmont', 'NC'),
('Sara', 'Wilson', 0, '7045552222', 'sara@example.com', 'swilson', 'pass123', '321 Elm St', 'Charlotte', 'NC'),
('David', 'Lee', 1, '7045553333', 'david@example.com', 'dlee', 'pass123', '654 Maple Dr', 'Gastonia', 'NC');

INSERT INTO staff
(sfirst_name, slast_name, username, password, email, phone_number)
VALUES
('Alex', 'Barber', 'abarber', 'pass123', 'alex@shop.com', '7041112222'),
('Chris', 'Fade', 'cfade', 'pass123', 'chris@shop.com', '7043334444'),
('Taylor', 'Cutz', 'tcutz', 'pass123', 'taylor@shop.com', '7045556666'),
('Jordan', 'Style', 'jstyle', 'pass123', 'jordan@shop.com', '7047778888'),
('Morgan', 'Clip', 'mclip', 'pass123', 'morgan@shop.com', '7049990000');

INSERT INTO haircut_types
(htype, description, htypeCost)
VALUES
('Basic Cut', 'Simple haircut', 20.00),
('Fade', 'Skin fade haircut', 30.00),
('Deluxe Cut', 'Cut + styling', 40.00),
('Buzz Cut', 'Very short cut', 15.00),
('Kids Cut', 'Haircut for children', 18.00);

INSERT INTO hairwash_types
(hwtype, description, hwcost)
VALUES
('Basic Wash', 'Quick wash', 10),
('Deluxe Wash', 'Wash + scalp massage', 20),
('Premium Wash', 'Wash + treatment', 25),
('Quick Rinse', 'Fast rinse only', 5),
('Deep Clean', 'Intensive clean', 30);

INSERT INTO beard_trims
(beardtrim, description, beardtrimcost)
VALUES
('Line Up', 'Shape and edge beard', 15),
('Full Trim', 'Complete beard trim', 25),
('Goatee Trim', 'Trim goatee style', 12),
('Stubble Trim', 'Light trim', 10),
('Luxury Trim', 'Trim + conditioning', 30);

INSERT INTO membership_types
(mtype, description, mtypeCost)
VALUES
('Basic Membership', '1 haircut/month', 25.00),
('Premium Membership', 'Unlimited cuts', 60.00),
('Student Membership', 'Discounted cuts', 20.00),
('Family Plan', 'Up to 4 members', 80.00),
('VIP Membership', 'Priority booking + extras', 100.00);

INSERT INTO products
(product, description, productCost)
VALUES
('Hair Gel', 'Strong hold gel', 12.99),
('Shampoo', 'Organic shampoo', 15.99),
('Beard Oil', 'Conditioning oil', 18.50),
('Hair Spray', 'Long hold spray', 14.25),
('Comb Set', 'Professional comb kit', 9.99);

INSERT INTO appointments
(CustomerID, HTypeID, StaffID, appointmentDate, appointmentTime, address, city, state)
VALUES
(1, 1, 1, '2026-04-25', '10:00:00', '123 Main St', 'Charlotte', 'NC'),
(2, 2, 2, '2026-04-26', '14:30:00', '456 Oak Ave', 'Gastonia', 'NC'),
(3, 3, 3, '2026-04-27', '09:00:00', '789 Pine Rd', 'Belmont', 'NC'),
(4, 4, 4, '2026-04-28', '11:15:00', '321 Elm St', 'Charlotte', 'NC'),
(5, 5, 5, '2026-04-29', '16:45:00', '654 Maple Dr', 'Gastonia', 'NC');

INSERT INTO orders
(CustomerID, HTypeID, MTypeID, ProductID, AppointmentID, orderCost, HWTypesID, BeardTrimID, PaymentMethod, cardNumber, expiration_date)
VALUES
(1, 1, 1, 1, 1, 57.99, 1, 1, 'Card', 123456789, '2027-01-01'),
(2, 2, NULL, 2, 2, 45.99, 2, NULL, 'Cash', NULL, NULL),
(3, 3, 2, 3, 3, 83.50, 3, 2, 'Card', 987654321, '2028-05-01'),
(4, 4, 3, 4, 4, 39.25, 4, 3, 'Card', 555666777, '2027-09-01'),
(5, 5, 4, 5, 5, 49.99, 5, 4, 'Cash', NULL, NULL);

INSERT INTO refunds
(refundReason, refundAmount)
VALUES
('Customer unhappy', 20.00),
('Overcharge correction', 10.00),
('Service issue', 15.00),
('Late appointment', 8.00),
('Product defect', 12.50);

INSERT INTO order_details
(OrderID, RefundID, CostBeforeTax, Tax, CostAfterTax)
VALUES
(1, NULL, 50.00, 7.99, 57.99),
(2, 1, 40.00, 5.99, 45.99),
(3, NULL, 75.00, 8.50, 83.50),
(4, 2, 35.00, 4.25, 39.25),
(5, 3, 45.00, 4.99, 49.99);