
## 🧠 How the Streamlit App Simulates Real-World Fraud Detection

### 🔒 About the Dataset

The credit card fraud dataset used in this project is sourced from real-world European card transactions. To protect sensitive user and merchant information, the data was **anonymized using Principal Component Analysis (PCA)**. As a result, most of the original features have been transformed into **28 principal components** (`V1` to `V28`), which retain important behavioral and transactional patterns but cannot be reverse-engineered.

---

### 🧮 Why the Model Uses V1–V28

Since the original features (like merchant ID, transaction type, device info, etc.) were not available, the model was trained **exclusively** on these PCA-transformed features:
- `Time` (seconds since first transaction)
- `Amount` (transaction value)
- `V1` to `V28` (anonymized components)

Therefore, any input to the trained model must match this structure. In a production environment, these values would be generated behind the scenes from raw transaction data.

---

### 🧪 Why the App Requires Manual Input for V1–V28

In this Streamlit app:
- We **simulate the backend pipeline** by asking users to manually input values for `V1` to `V28`.
- This allows us to test how the trained model responds to various hypothetical transaction scenarios.
- While this is not how a real-world user would interact with the system, it provides a **realistic demonstration of the fraud detection logic** and model behavior.

---

### 🛠️ In a Real Production Pipeline

In an actual deployment:
1. Raw transaction data (merchant info, geolocation, user history, etc.) would be collected in real-time.
2. A **feature engineering pipeline** would transform this raw data into the same structure used during model training.
3. The **PCA transformation** (saved from training) would be applied to generate `V1` to `V28`.
4. The transformed features would be passed to the trained model for prediction — seamlessly, without user input.

---

### 📌 Conclusion

This app demonstrates the final step of the real-world fraud detection pipeline — given preprocessed (PCA-transformed) features, it predicts whether a transaction is likely to be fraudulent. The manual input of V1–V28 is only for **demonstration and testing purposes** in the absence of access to the original feature pipeline.
