# Brent Oil Price & Structural Change Point Analytics

An end-to-end data science and Bayesian analytics suite designed to quantify structural breaks in historical Brent Crude Oil prices (1987–2022) and correlate them with major geopolitical events, OPEC decisions, and global macroeconomic shocks.

---

## 📌 Executive Summary
* **Historical Horizon:** Analyzes **9,011 daily trading records** spanning May 20, 1987 to November 14, 2022.
* **Core Insight:** Uncovers sharp structural regime shifts using Bayesian Markov Chain Monte Carlo (MCMC) inference via **PyMC**.
* **Key Event Impact:** Isolates the **2014 OPEC Production Non-Cut Decision** ($\tau = 2014\text{-}11\text{-}26$), quantifying a persistent baseline price drop from **$105.77/bbl** ($\mu_1$) down to **$48.69/bbl** ($\mu_2$)—a **-53.96% (-$57.08/bbl)** market reduction.
* **Interactive Dashboard:** Includes a full-stack Flask API and React (Vite + Recharts + Tailwind CSS) web application for interactive stakeholder exploration.

---

## 🏗 Repository Architecture

```text
Change-Point-Analysis/
├── data/
│   ├── raw/                   # Historical Brent price CSV data
│   └── processed/             # Cleaned event catalogs and resampled series
├── notebooks/                 # Exploratory & PyMC modeling notebooks
│   ├── Task1_EDA_Stationarity.ipynb
│   └── Task2_Bayesian_Change_Point.ipynb
├── src/                       # Reusable Python modules
│   ├── data_loader.py         # Data cleaning & log return transforms
│   ├── stats_tests.py         # ADF, KPSS, and stationarity utilities
│   └── pymc_models.py         # PyMC change point model builders
├── dashboard/                 # Task 3: Full-Stack Web Application
│   ├── backend/               # Flask REST API
│   │   ├── app.py             # Endpoint routes & CORS handling
│   │   ├── requirements.txt   # Backend dependencies
│   │   └── data/              # Exported JSON datasets for API
│   └── frontend/              # React (Vite) Application
│       ├── package.json       # React dependencies
│       ├── vite.config.js     # Vite & Tailwind CSS v4 config
│       └── src/               # React components & Recharts visualizations
├── export_dashboard_data.py   # Data pipeline export script for dashboard
├── DASHBOARD_README.md        # Detailed dashboard setup & run instructions
├── requirements.txt           # Main Python analytics environment dependencies
└── README.md                  # Master repository documentation