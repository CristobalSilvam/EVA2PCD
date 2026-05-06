import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """
    Carga el dataset, realiza limpieza básica y optimiza los tipos de datos.
    
    Args:
        file_path (str): Ruta al archivo CSV.
        
    Returns:
        pd.DataFrame: DataFrame limpio y optimizado.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {file_path}")
        return None

    # 1. Conversión de fechas
    df['month'] = pd.to_datetime(df['month'])
    
    # 2. Optimización de memoria: Convertir a categóricas
    cat_cols = ['conflict_phase', 'airline', 'iata_code', 'origin_city', 
                'destination_city', 'aircraft_type', 'rerouted', 'flight_cancelled']
    
    for col in cat_cols:
        df[col] = df[col].astype('category')
        
    # 3. Eliminar duplicados si existen
    df = df.drop_duplicates()
    
    return df

def apply_feature_engineering(df):
    """
    Genera nuevas características (features) útiles para los modelos.
    
    Args:
        df (pd.DataFrame): DataFrame limpio.
        
    Returns:
        pd.DataFrame: DataFrame con nuevas columnas.
    """
    # Evitar SettingWithCopyWarning
    df = df.copy()
    
    # Métrica de eficiencia: Costo de combustible por kilómetro
    df['fuel_cost_per_km'] = np.where(
        df['actual_distance_km'] > 0, 
        df['total_fuel_cost_usd'] / df['actual_distance_km'], 
        0
    )
    
    # Métrica de rentabilidad: Ingreso por pasajero
    df['revenue_per_passenger'] = np.where(
        df['estimated_passengers'] > 0,
        df['route_revenue_usd'] / df['estimated_passengers'],
        0
    )
    
    return df