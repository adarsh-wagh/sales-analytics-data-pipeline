-- =============================================
-- Sales Analytics Data Pipeline
-- Bronze Layer - Table Creation
-- Database: sales_dw
-- =============================================

DROP TABLE IF EXISTS bronze.cust_info CASCADE;

CREATE TABLE bronze.cust_info (
    cst_id              INTEGER,
    cst_key             VARCHAR(50),
    cst_firstname       VARCHAR(50),
    cst_lastname        VARCHAR(50),
    cst_marital_status  VARCHAR(50),
    cst_gndr            VARCHAR(50),
    cst_create_date     DATE,
	dwh_load_date 		TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

--------------------------------------------------

DROP TABLE IF EXISTS bronze.prd_info CASCADE;

CREATE TABLE bronze.prd_info (
    prd_id          INTEGER,
    prd_key         VARCHAR(50),
    prd_nm          VARCHAR(50),
    prd_cost        INTEGER,
    prd_line        VARCHAR(50),
    prd_start_dt    TIMESTAMP,
    prd_end_dt      TIMESTAMP,
	dwh_load_date	TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

--------------------------------------------------

DROP TABLE IF EXISTS bronze.sales_details CASCADE;

CREATE TABLE bronze.sales_details (
    sls_ord_num     VARCHAR(50),
    sls_prd_key     VARCHAR(50),
    sls_cust_id     INTEGER,
    sls_order_dt    INTEGER,
    sls_ship_dt     INTEGER,
    sls_due_dt      INTEGER,
    sls_sales       INTEGER,
    sls_quantity    INTEGER,
    sls_price       INTEGER,
	dwh_load_date 	TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

--------------------------------------------------

DROP TABLE IF EXISTS bronze.cust_az12 CASCADE;

CREATE TABLE bronze.cust_az12 (
    cid         	VARCHAR(50),
    bdate       	DATE,
    gen         	VARCHAR(50),
	dwh_load_date 	TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

--------------------------------------------------

DROP TABLE IF EXISTS bronze.loc_a101 CASCADE;

CREATE TABLE bronze.loc_a101 (
    cid         	VARCHAR(50),
    cntry       	VARCHAR(50),
	dwh_load_date 	TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

--------------------------------------------------

DROP TABLE IF EXISTS bronze.px_cat_g1v2 CASCADE;

CREATE TABLE bronze.px_cat_g1v2 (
    id              VARCHAR(50),
    cat             VARCHAR(50),
    subcat          VARCHAR(50),
    maintenance     VARCHAR(50),
	dwh_load_date 	TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);