pip install pyathena

from pyathena import connect
import pandas as pd

conn = connect(aws_access_key_id='',
               aws_secret_access_key='',
               s3_staging_dir='s3://boletos789788789794/costumers/' ,
               region_name='us-east-1')
df = pd.read_sql("SELECT * FROM bancoo.costumers limit 10", conn)
print(df.head()) 
