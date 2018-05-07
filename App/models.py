from . import app, db

class society(db.Model):
	__tablename__="society"
	society_id   = db.Column(db.Integer, primary_key=True)
	society_name = db.Column(db.String(255), nullable=False)
	region       = db.Column(db.String(127), nullable=False)
	city         = db.Column(db.String(127), nullable=False)
	state        = db.Column(db.String(127), nullable=False)
	area         = db.Column(db.Integer, nullable=False)

class wing(db.Model):
	__tablename__="wing"
	wing_id      = db.Column(db.Integer, primary_key=True)
	society_id   = db.Column(db.Integer, db.ForeignKey('society.society_id'), nullable=False)
	wing_name    = db.Column(db.String(15), nullable=False)
	no_of_floors = db.Column(db.Integer, nullable=False)
	total_area   = db.Column(db.Integer, nullable=False)

class flat(db.Model):
	__tablename__="flat"
	flat_id  = db.Column(db.Integer, primary_key=True)
	wing_id  = db.Column(db.Integer, db.ForeignKey('wing.wing_id'), nullable=False)
	flat_num = db.Column(db.Integer, nullable=False)
	facing   = db.Column(db.String(31), nullable=False)
	area     = db.Column(db.Integer, nullable=False)
	BHK      = db.Column(db.Numeric(precision=2, scale=1), nullable=False)
	floor_no = db.Column(db.Integer, nullable=False)
	price    = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

class resident(db.Model):
	__tablename__="resident"
	resident_id   = db.Column(db.Integer, primary_key=True)
	flat_id       = db.Column(db.Integer, db.ForeignKey('flat.flat_id'), nullable=False)
	resident_name = db.Column(db.String(127), nullable=False)
	contact       = db.Column(db.Numeric(precision = 10,asdecimal=False), nullable=False)

class committee_member(db.Model):
	__tablename__="committee_member"
	resident_id   = db.Column(db.Integer, primary_key=True)
	wing_id       = db.Column(db.Integer, db.ForeignKey('wing.wing_id'), nullable=False)
	flat_no       = db.Column(db.Integer, nullable=False)
	post          = db.Column(db.String(31), nullable=False)

class account(db.Model):
	__tablename__="account"
	acc_name = db.Column(db.String(14), primary_key=True)
	flat_id  = db.Column(db.Integer, db.ForeignKey('flat.flat_id'), nullable=False)
	acc_pass = db.Column(db.String(15), nullable=False)
	owner_name   = db.Column(db.String(127), nullable=False)
	pending_dues = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
	profile_img  = db.Column(db.LargeBinary)

class admin(db.Model):
	resident_id   = db.Column(db.Integer, primary_key=True)
	society_id    = db.Column(db.Integer, db.ForeignKey('society.society_id'), nullable=False)
	admin_pass    = db.Column(db.String(15), nullable=False)

class document(db.Model):
	__tablename__="document"
	doc_id      = db.Column(db.Integer, primary_key=True)
	flat_id     = db.Column(db.Integer, db.ForeignKey('flat.flat_id'), nullable=False)
	doc_name    = db.Column(db.String(31), nullable=False)
	upload_date = db.Column(db.Date, nullable=False)
	path        = db.Column(db.String(255), nullable=False)

class facility(db.Model):
	__tablename__="facility"
	society_id     = db.Column(db.Integer, primary_key=True)
	facility_name  = db.Column(db.String(31), primary_key=True)
	price_per_hour = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
	#start_time     = db.Column(Time(), )
	#end_time

class issues(db.Model):
	__tablename__="issues"
	issue_id     = db.Column(db.Integer, primary_key=True)
	acc_name     = db.Column(db.String(14), db.ForeignKey('account.acc_name'), nullable=False)
	issue_date   = db.Column(db.Date, nullable=False)
	issues_desc  = db.Column(db.String(255), nullable=False)
	reported_by  = db.Column(db.String(127), nullable=False)
	related      = db.Column(db.String(31), nullable=False)

class maintenance_bill(db.Model):
	__tablename__="maintenance_bill"
	bill_num        = db.Column(db.Integer, primary_key=True)
	flat_id         = db.Column(db.Integer, db.ForeignKey('flat.flat_id'), nullable=False)
	bill_date       = db.Column(db.Date, nullable=False)
	water_charges   = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	property_tax    = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	elec_charges    = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	sinking_fund    = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	parking_charges = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	noc             = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	insurance       = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	other           = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
	due_date        = db.Column(db.Date, nullable=False)
	down_doc        = db.Column(db.String(255), nullable=False)

class notices(db.Model):
	__tablename__="notices"
	notice_id               = db.Column(db.Integer, primary_key=True)
	society_id              = db.Column(db.Integer, db.ForeignKey('society.society_id'), nullable=False)
	notice_header           = db.Column(db.String(255), nullable=False)
	notice_date             = db.Column(db.Date, nullable=False)
	notice_desc             = db.Column(db.String(255), nullable=False)
	valid_for_all_buildings = db.Column(db.Integer)

