import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class TideForecast:
    def __init__(self):
        self.model = LinearRegression()
        
    def generate_sample_data(self, days=30):
        """Genera datos de muestra para demostración"""
        dates = pd.date_range(start=datetime.now(), periods=days*24, freq='H')
        # Simulación de datos de marea usando una función sinusoidal
        base_tide = 2.0  # altura base de la marea en metros
        amplitude = 1.5  # amplitud de la marea
        period = 12.4   # período de la marea en horas
        
        tides = base_tide + amplitude * np.sin(2 * np.pi * np.arange(len(dates)) / period)
        noise = np.random.normal(0, 0.1, len(dates))
        tides += noise
        
        return pd.DataFrame({
            'datetime': dates,
            'tide_height': tides
        })
    
    def train_model(self, data):
        """Entrena el modelo con datos históricos"""
        X = np.arange(len(data)).reshape(-1, 1)
        y = data['tide_height'].values
        self.model.fit(X, y)
        
    def predict(self, hours_ahead=24):
        """Realiza predicciones para las próximas horas"""
        last_index = len(self.historical_data)
        future_indices = np.arange(last_index, last_index + hours_ahead).reshape(-1, 1)
        predictions = self.model.predict(future_indices)
        
        future_dates = pd.date_range(
            start=self.historical_data['datetime'].iloc[-1] + timedelta(hours=1),
            periods=hours_ahead,
            freq='H'
        )
        
        return pd.DataFrame({
            'datetime': future_dates,
            'predicted_height': predictions
        })
    
    def plot_forecast(self, historical_data, forecast_data):
        """Visualiza los datos históricos y el pronóstico"""
        plt.figure(figsize=(12, 6))
        plt.plot(historical_data['datetime'], historical_data['tide_height'], 
                label='Datos históricos', color='blue')
        plt.plot(forecast_data['datetime'], forecast_data['predicted_height'], 
                label='Pronóstico', color='red', linestyle='--')
        plt.title('Pronóstico de Mareas')
        plt.xlabel('Fecha y Hora')
        plt.ylabel('Altura de la marea (m)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    # Crear instancia del pronosticador
    forecaster = TideForecast()
    
    # Generar datos de muestra
    historical_data = forecaster.generate_sample_data(days=30)
    forecaster.historical_data = historical_data
    
    # Entrenar el modelo
    forecaster.train_model(historical_data)
    
    # Realizar pronóstico para las próximas 24 horas
    forecast_data = forecaster.predict(hours_ahead=24)
    
    # Visualizar resultados
    forecaster.plot_forecast(historical_data, forecast_data)
    
    # Mostrar pronóstico para las próximas horas
    print("\nPronóstico de mareas para las próximas 24 horas:")
    print(forecast_data.to_string(index=False))

if __name__ == "__main__":
    main() 