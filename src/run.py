from src import db
import pandas as pd

import datetime

from utils import get_all_countries, get_country_info, encrypt_string



def main():
    countries = get_all_countries()
    data = []
    for country in countries:
        start_time = datetime.datetime.now()
        country_info = get_country_info(country)

        # skips countries that doesn't have the info needed
        if not country_info:
            continue
        country_name, country_region, country_languages = country_info
        
        middle_time = datetime.datetime.now() - start_time
        language_time = datetime.timedelta(0)
        for language in country_languages:
            
            sha1_encrypted_languaje = encrypt_string(language)
            end_time = datetime.datetime.now()

            final_time = end_time - start_time - language_time
            if language_time == 0:
                language_time = final_time
            else:
                final_time + middle_time

            final_time = final_time.total_seconds() * 1000
            data.append(
                [country_name, country_region, sha1_encrypted_languaje, final_time]
            )
    df = pd.DataFrame(data, columns=['Región', 'City Name', 'Language', 'Time'])
    
    print(
        f"""
        Tiempo Promedio: {df['Time'].mean()} ms
        Tiempo Máximo: {df['Time'].max()} ms
        Tiempo Mínimo: {df['Time'].min()} ms
        """
    )
    db.save_dataframe(df)
    df.to_json('data.json', orient='records', force_ascii=False)