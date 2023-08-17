# Inspired by: https://pynative.com/python-postgresql-tutorial/

import os
import logging
import psycopg2

level = os.getenv("LOGLEVEL", "INFO").upper()
logging.basicConfig(format="%(asctime)s %(levelname)-8s %(name)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=level)

logger = logging.getLogger("client")

user = os.getenv("POSTGRES_USER", "scientist")
password = os.getenv("POSTGRES_PASSWORD", "C473rp1ll4r")
host = os.getenv("POSTGRES_HOST", "db")
port = os.getenv("POSTGRES_PORT", "5432")
database = os.getenv("POSTGRES_DB", "datascience")

try:
    connection = psycopg2.connect(user = user,
                                  password = password,
                                  host = host,
                                  port = port,
                                  database = database)

    cursor = connection.cursor()

    # Print PostgreSQL Connection properties
    logger.info("Properties: {}\n".format(connection.get_dsn_parameters()))

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    logger.info("You are connected to {}\n".format(record))

except (Exception, psycopg2.Error, psycopg2.OperationalError) as error :
    logger.error("Error while connecting to PostgreSQL: {}".format(error))

else:
    # Close database connection
    cursor.close()
    connection.close()
    logger.info("PostgreSQL connection was closed")
