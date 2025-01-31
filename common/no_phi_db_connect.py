from    contextlib  import  contextmanager
import  psycopg2    as      db


@contextmanager
def no_phi_conn():
    con = db.connect(
                        database    =   "beacon_nophi"
                        ,user       =   "mlazaldi"
                        ,password   =   "Aknglas@7Asfb!Gem"
                        ,host       =   "gemini-nophi.coavvdyjgjyx.us-east-1.rds.amazonaws.com"
                        ,port       =   5432
                     )
    try:
        yield con
    finally:
        con.commit()
        con.close()