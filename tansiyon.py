import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

def tansiyon_coz(tansiyon_str):
    try:
        sistolik,diyastolik = tansiyon_str.split('/')
        return int(sistolik), int(diyastolik)
    except Exception as hata:
        return np.nan, np.nan
    
def main():
    df =pd.read_excel('tansiyon.xlsx')

    df[['sabah_sistolik','sabah_diyastolik']] = df['Sabah Tansiyon'].apply(lambda x: pd.Series(tansiyon_coz(x)))
    df[['aksam_sistolik','aksam_diyastolik']] = df['Akşam Tansiyon'].apply(lambda x: pd.Series(tansiyon_coz(x)))

    ozellikler = df[['sabah_sistolik','sabah_diyastolik','aksam_sistolik','aksam_diyastolik']].dropna()

    kmeans = KMeans(n_clusters=2, random_state=42,)
    
    kumeler = kmeans.fit_predict(ozellikler)

    ozellikler['cluster'] = kumeler

    kume_ortalamalari = ozellikler.groupby('cluster').mean()[['sabah_sistolik','aksam_sistolik']]
    riskli_kume = kume_ortalamalari.mean(axis=1).idxmax()

    ozellikler['risk'] = ozellikler['cluster'].apply(lambda x: 'Risk' if x == riskli_kume else 'Normal')

    df = df.join(ozellikler['risk'])

    risk_sayisi = df['risk'].value_counts().get('Risk',0)
    toplam = df['risk'].count()
    genel_risk = 'Yüksek Tansiyon / Kalp Riski' if risk_sayisi/toplam >= 0.5 else 'Normal Tansiyon'

    print("Günlük Risk Durumları")
    print(df[['Tarih','risk']])
    print("\nGenel Değerlendirme: ",genel_risk)

if __name__ == '__main__':
    main()