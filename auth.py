
import os
from supabase import create_client, Client

url: str = os.environ.get("https://iutakyyvmkuyrxxtjgek.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Iml1dGFreXl2bWt1eXJ4eHRqZ2VrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg1Njc0OTcsImV4cCI6MjAzNDE0MzQ5N30.fQpY5hZvgIpzdoYiUYYb6Ssuc2W_LfS8eGWrd6O15s8")
supabase: Client = create_client(url, key)


