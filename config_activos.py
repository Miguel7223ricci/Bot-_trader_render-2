CONFIG = {
    "modelo_path": "modelo_trained_rf_pro.pkl",
    "intervalo": "4h",
    "periodo": "60",  # últimos 60 velas de 4h
    "pausa_horas": 4,
    "umbral_confianza": 0.55,
    "activos": {
        # Acciones estadounidenses
        "Apple Inc": "AAPL",
        "Tesla Inc": "TSLA",
        "CoroWare Inc": "COWI",
        "Microsoft Corp.": "MSFT",
        "Alphabet Inc.": "GOOG",
        "Amazon.com Inc.": "AMZN",
        "Meta Platforms Inc.": "META",
        "Intel Corp.": "INTC",

        # ETFs estadounidenses
        "SPDR S&P 500 ETF Trust": "SPY",
        "Direxion Semiconductor Bear 3X": "SOXS",
        "UltraPro Short QQQ": "SQQQ",
        "GraniteShares COIN 1.5x ETF": "CONL",
        "Invesco QQQ Trust": "QQQ",
        "iShares Russell 2000": "IWM",
        "iShares Emerging Markets": "EEM",
        "SPDR Dow Jones Industrial": "DIA",

        
    }
}
