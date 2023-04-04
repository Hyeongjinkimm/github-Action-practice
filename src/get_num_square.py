import os

num = os.environment.get("INPUT_NUM")

if num:
    try:
       num = int(num)
    expect Exception:
       exit()
else:
    num = 1
    
print(f"::set-output name=num_squared::{num**2}")
