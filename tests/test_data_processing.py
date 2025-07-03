import pandas as pd
from src.create_proxy_label import create_rfm_proxy_target

def test_create_rfm_proxy_target_output_format():
    data = {
        'CustomerId': ['C1', 'C1', 'C2', 'C2'],
        'TransactionId': [101, 102, 201, 202],
        'Amount': [100, 200, 50, 75],
        'TransactionStartTime': ['2025-06-01', '2025-06-10', '2025-06-05', '2025-06-15']
    }
    df = pd.DataFrame(data)
    df['CustomerId'] = df['CustomerId'].str.extract(r'(\d+)').fillna(0).astype(int)

    result = create_rfm_proxy_target(df)
    assert 'is_high_risk' in result.columns
    assert set(result.columns) == {'CustomerId', 'is_high_risk'}

def test_proxy_high_risk_values():
    data = {
        'CustomerId': [1],
        'TransactionId': [101],
        'Amount': [100],
        'TransactionStartTime': ['2025-06-01']
    }
    df = pd.DataFrame(data)
    result = create_rfm_proxy_target(df)
    assert result['is_high_risk'].isin([0, 1]).all()
