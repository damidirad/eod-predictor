from feature_schema import product_schema, account_schema

def validate_features(obj, feature, value, schema):
    if feature in schema:
        expected_type, constraints = schema[feature]

        if not isinstance(value, expected_type):
            raise ValueError(f"Feature '{feature}' must be of type {expected_type.__name__}")

        if expected_type == str:
            max_length = constraints.get('max_length')
            if max_length is not None and len(value) > max_length:
                raise ValueError(f"Feature '{feature}' must be at most {max_length} characters long")

        if 'not_null' in constraints and value is None:
            raise ValueError(f"Feature '{feature}' cannot be null")

        setattr(obj, feature, value)
    else:
        raise AttributeError(f"Unknown feature '{feature}'")
    
class Product:
    feature_schema = product_schema

    def __init__(self, **features):
        for feature, (_, constraints) in Product.feature_schema.items():
            if 'default' in constraints:
                setattr(self, feature, constraints['default'])

        for feature, value in features.items():
            validate_features(self, feature, value, Product.feature_schema)

class Account:
    feature_schema = account_schema

    def __init__(self, product, **features):
        self.product = product

        for feature, (_, constraints) in Account.feature_schema.items():
            if 'default' in constraints:
                setattr(self, feature, constraints['default'])

        for feature, value in features.items():
            validate_features(self, feature, value, Account.feature_schema)

class Bank:
    def __init__(self, name, loan_processing_time=None):
        self.name = name
        self.loan_processing_time = loan_processing_time
        self.products = []
        self.accounts = []

    def add_product(self, product):
        self.products.append(product)

    def add_account(self, account):
        if account.product in self.products:
            self.accounts.append(account)
        else:
            raise ValueError(f"Bank '{self.name}' has no product '{account.product.PRODUCTNAME}'")

