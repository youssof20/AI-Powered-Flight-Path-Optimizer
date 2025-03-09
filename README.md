# ✈️ AI-Powered Flight Path Optimizer 🚀

This project uses **AI techniques** to optimize flight paths for **efficiency, cost, and time**. It processes flight and airport data to find the **best routes** using advanced algorithms. Perfect for aviation enthusiasts, data scientists, and AI practitioners! 🌍

---

## 🎯 Features

- **📂 Load and preprocess** flight and airport data.
- **🤖 Optimize flight paths** using AI algorithms.
- **📊 Visualize optimized flight paths** with interactive graphs.
- **⚡ Lightweight and easy to use**.

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/youssof20/AI-Powered-Flight-Path-Optimizer.git
   cd AI-Powered-Flight-Path-Optimizer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project**:
   ```bash
   bash run.sh
   ```

---

## 🚀 Usage

1. Place your flight and airport data in the `data/` directory.
2. Run the `main.py` script to optimize flight paths:
   ```bash
   python src/main.py
   ```
3. View the optimized flight paths and visualizations.

---

## 📂 Data Format

### `airports.csv`
Contains airport details:
- **IATA code**: Unique airport code (e.g., `JFK`).
- **Name**: Airport name.
- **Latitude**: Geographic latitude.
- **Longitude**: Geographic longitude.

Example:
```csv
iata_code,name,latitude,longitude
JFK,John F. Kennedy International Airport,40.639801,-73.7789
LAX,Los Angeles International Airport,33.9425,-118.408
```

### `flights.csv`
Contains flight details:
- **Origin**: IATA code of the origin airport.
- **Destination**: IATA code of the destination airport.
- **Distance**: Flight distance in miles.
- **Duration**: Flight duration in minutes.

Example:
```csv
origin,destination,distance,duration
JFK,LAX,2475,360
JFK,ATL,760,120
```

---

## 🧪 Testing

Run the test suite to ensure everything works as expected:
```bash
python -m unittest discover tests/
```

---

## 🤝 Contributing

We welcome contributions! Here’s how you can help:

1. **Fork the repository**.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your awesome feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a **pull request** and describe your changes.

For major changes, please open an **issue** first to discuss your ideas.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to the open-source community for amazing libraries like `networkx`, `pandas`, and `matplotlib`.
- Inspired by real-world flight optimization challenges.

---

Enjoy optimizing flight paths with AI! ✈️🤖
