import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Memuat model yang telah dilatih
@st.cache_data
def load_model():
    with open('HasilModel_air.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Validasi input terhadap standar internasional
def check_standards(input_data):
    standards = {
        'ph': (6.5, 8.5),
        'Hardness': (0, 300),
        'Solids': (0, 500),
        'Chloramines': (0, 4),
        'Sulfate': (0, 250),
        'Conductivity': (0, 800),
        'Organic_carbon': (0, 5),
        'Trihalomethanes': (0, 80),
        'Turbidity': (0, 1),
    }
    results = {"valid": True, "messages": []}
    for feature, (min_val, max_val) in standards.items():
        if not (min_val <= input_data[feature][0] <= max_val):
            results["valid"] = False
            results["messages"].append(f"{feature} berada di luar batas standar ({min_val} - {max_val}).")
    return results

# Sistem peringatan otomatis
def check_warnings(input_data):
    warnings = []
    standards = {
        'ph': (6.5, 8.5),
        'Hardness': (0, 300),
        'Solids': (0, 500),
        'Chloramines': (0, 4),
        'Sulfate': (0, 250),
        'Conductivity': (0, 800),
        'Organic_carbon': (0, 5),
        'Trihalomethanes': (0, 80),
        'Turbidity': (0, 1),
    }

    for feature, (min_val, max_val) in standards.items():
        value = input_data[feature][0]
        if value < min_val or value > max_val:
            warnings.append(f"\u26A0\uFE0F {feature}: {value} berada di luar standar ({min_val} - {max_val})")
        elif abs(value - min_val) <= 0.1 * (max_val - min_val) or abs(value - max_val) <= 0.1 * (max_val - min_val):
            warnings.append(f"\u26A0\uFE0F {feature}: {value} mendekati batas standar ({min_val} - {max_val})")
    return warnings

# Rekomendasi solusi
def get_mitigation_recommendations(input_data):
    solutions = {
        'ph': "Tambahkan bahan kimia untuk menyesuaikan pH.",
        'Hardness': "Gunakan softener untuk mengurangi kekerasan air.",
        'Solids': "Gunakan filtrasi untuk mengurangi zat padat.",
        'Chloramines': "Tambahkan filtrasi karbon aktif untuk mengurangi kloramin.",
        'Sulfate': "Gunakan reverse osmosis untuk mengurangi kadar sulfat.",
        'Conductivity': "Perbaiki sumber air untuk mengurangi konduktivitas.",
        'Organic_carbon': "Gunakan filtrasi karbon aktif.",
        'Trihalomethanes': "Gunakan teknologi dechlorination.",
        'Turbidity': "Gunakan filtrasi fisik untuk mengurangi kekeruhan."
    }

    recommendations = []
    standards = {
        'ph': (6.5, 8.5),
        'Hardness': (0, 300),
        'Solids': (0, 500),
        'Chloramines': (0, 4),
        'Sulfate': (0, 250),
        'Conductivity': (0, 800),
        'Organic_carbon': (0, 5),
        'Trihalomethanes': (0, 80),
        'Turbidity': (0, 1),
    }

    for feature, (min_val, max_val) in standards.items():
        if not (min_val <= input_data[feature][0] <= max_val):
            recommendations.append(f"{feature}: {solutions.get(feature, 'Tidak ada rekomendasi.')}")
    return recommendations

# Fungsi untuk menentukan faktor-faktor yang mempengaruhi kualitas air
def determine_factors(input_data):
    factors = []
    if input_data['ph'][0] < 6.5:
        factors.append("pH air terlalu rendah. Ini dapat mempengaruhi rasa dan keamanan air.")
    elif input_data['ph'][0] > 8.5:
        factors.append("pH air terlalu tinggi. Ini dapat mempengaruhi rasa dan menyebabkan korosi pada pipa.")
    
    if input_data['Hardness'][0] > 300:
        factors.append("Kekerasan air terlalu tinggi, yang dapat menyebabkan penumpukan kalsium dan magnesium.")
    
    if input_data['Turbidity'][0] > 1.0:
        factors.append("Kekeruhan air terlalu tinggi, yang menunjukkan adanya partikel terlarut yang dapat mempengaruhi kualitas.")
    
    if input_data['Chloramines'][0] > 4.0:
        factors.append("Kadar kloramin terlalu tinggi, yang dapat menyebabkan rasa tidak enak pada air.")
    
    return factors

# Input data pengguna
def user_input_features():
    st.sidebar.write("## Input Data")
    st.sidebar.write("Masukkan parameter kualitas air pada form berikut sesuai data Anda:")

    with st.sidebar.form(key='input_form'):
        ph = st.number_input('pH (contoh: 7.0)', 0.0, 14.0, 7.0)
        hardness = st.number_input('Kekerasan (Hardness) (contoh: 150)', 0, 500, 150)
        solids = st.number_input('Zat Padat (Solids) (contoh: 500)', 0, 1000, 500)
        chloramines = st.number_input('Kloramin (Chloramines) (contoh: 4.0)', 0.0, 10.0, 4.0)
        sulfate = st.number_input('Sulfat (Sulfate) (contoh: 200)', 0, 400, 200)
        conductivity = st.number_input('Konduktivitas (Conductivity) (contoh: 500)', 0, 1500, 500)
        organic_carbon = st.number_input('Karbon Organik (Organic Carbon) (contoh: 5.0)', 0.0, 10.0, 5.0)
        trihalomethanes = st.number_input('Trihalometan (Trihalomethanes) (contoh: 80.0)', 0.0, 200.0, 80.0)
        turbidity = st.number_input('Kekeruhan (Turbidity) (contoh: 1.0)', 0.0, 5.0, 1.0)

        submit_button = st.form_submit_button(label='Submit Data')

    data = {
        'ph': ph,
        'Hardness': hardness,
        'Solids': solids,
        'Chloramines': chloramines,
        'Sulfate': sulfate,
        'Conductivity': conductivity,
        'Organic_carbon': organic_carbon,
        'Trihalomethanes': trihalomethanes,
        'Turbidity': turbidity
    }

    return pd.DataFrame(data, index=[0])

# Streamlit Antarmuka
st.title("Prediksi Kualitas Air")

# Memuat model
model = load_model()

# Input data pengguna
input_df = user_input_features()

# Validasi standar internasional
validation = check_standards(input_df)

# Sistem peringatan otomatis
warnings = check_warnings(input_df)

st.write("### Parameter Data")
st.write(input_df)

if warnings:
    st.write("### \u26A0\uFE0F Peringatan Parameter")
    for warning in warnings:
        st.write(warning)

if validation["valid"]:
    st.write("### Semua parameter memenuhi standar internasional!")
    st.write("Air **layak diminum** berdasarkan standar internasional.")
else:
    st.write("### Validasi Standar Kualitas Air:")
    for message in validation["messages"]:
        st.write(f"- {message}")
    st.write("Air **tidak layak diminum** karena parameter di atas tidak memenuhi standar.")

# Menentukan faktor yang berpengaruh dan rekomendasi solusi
factors = determine_factors(input_df)
if factors:
    st.write("### Faktor yang Mempengaruhi Kualitas Air")
    for factor in factors:
        st.write(f"- {factor}")

recommendations = get_mitigation_recommendations(input_df)

if recommendations:
    st.write("### \U0001F4A1 Rekomendasi Mitigasi")
    for recommendation in recommendations:
        st.write(f"- {recommendation}")

# Tombol "Lihat Hasil"
if st.button("Lihat Hasil"):
    st.write("### Prediksi Berdasarkan Model:")
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    if validation["valid"] and prediction[0] == 0:
        st.write("Prediksi: Air **tidak layak diminum** meskipun memenuhi standar internasional.")
        st.write("### Kemungkinan Alasan:")
        st.write("- Model mendeteksi pola kompleks pada parameter yang tidak tercakup dalam standar internasional.")
        st.write("- Bisa jadi terdapat faktor tersembunyi dalam data yang tidak tercakup dalam validasi standar.")
    elif not validation["valid"] and prediction[0] == 1:
        st.write("Prediksi: Air **layak diminum** meskipun tidak memenuhi standar internasional.")
        st.write("### Kemungkinan Alasan:")
        st.write("- Model mungkin mengidentifikasi parameter yang lebih fleksibel dibandingkan standar internasional.")
        st.write("- Bisa jadi model telah dilatih pada data dengan toleransi yang lebih tinggi.")

    # Jika prediksi sesuai dengan validasi
    if prediction[0] == 1 and validation["valid"]:
        st.write("Prediksi: Air **layak diminum**.")
    elif prediction[0] == 0 and not validation["valid"]:
        st.write("Prediksi: Air **tidak layak diminum**.")

    st.write("### Probabilitas Prediksi:")
    st.write(f"Layak Minum: {prediction_proba[0][1]:.2f}")
    st.write(f"Tidak Layak Minum: {prediction_proba[0][0]:.2f}")

    # Grafik animasi
    fig = make_subplots(rows=1, cols=1)
    fig.add_trace(go.Bar(x=['Layak Minum', 'Tidak Layak Minum'],
                         y=[prediction_proba[0][1], prediction_proba[0][0]],
                         name="Probabilitas",
                         marker=dict(color=['green', 'red'])))
    fig.update_layout(title="Prediksi Probabilitas Kualitas Air",
                      xaxis_title="Status Air",
                      yaxis_title="Probabilitas",
                      showlegend=False,
                      updatemenus=[dict(type='buttons',
                                        showactive=False,
                                        buttons=[dict(label="Animate",
                                                     method="animate",
                                                     args=[None, dict(frame=dict(duration=1000, redraw=True), fromcurrent=True)])])])
    st.plotly_chart(fig, key="probability_chart")
