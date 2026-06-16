"""
AI Agent personas and their behaviors
"""


class ConsumerAgent:
    """Public-facing agent: friendly, high guardrails"""
    
    def __init__(self):
        self.name = "Consumer Assistant"
        self.guardrails = [
            "Never reveal wholesale or internal data",
            "Always provide market ranges, not exact prices",
            "Maintain friendly, supportive tone",
            "Don't mention competitor pricing"
        ]
    
    def get_valuation_response(self, vehicle_data):
        """Generate consumer-friendly valuation response"""
        # TODO: Implement with actual logic
        return f"Based on market data, your {vehicle_data.get('year')} {vehicle_data.get('make')} {vehicle_data.get('model')} is worth $9,999–$11,499."


class SalesAgent:
    """Internal sales agent: margin-focused, full data access"""
    
    def __init__(self):
        self.name = "Sales & Appraisal Companion"
        self.capabilities = [
            "Access historical appraisal data",
            "View repair cost estimates",
            "Analyze days-on-market metrics",
            "Calculate front-end gross profit"
        ]
    
    def get_negotiation_points(self, appraisal_data):
        """Generate data-driven negotiation insights"""
        # TODO: Implement with actual logic
        return f"Recommend appraisal of ${appraisal_data.get('predicted_value', 9999)}. Days on lot: {appraisal_data.get('days_on_lot', 'N/A')}."


class ExecutiveAgent:
    """Executive dashboard: strategic, macro-focused"""
    
    def __init__(self):
        self.name = "Executive Decision Support"
        self.focus_areas = [
            "Inventory capital utilization",
            "Average wholesale-to-retail turn time",
            "Projected monthly net margin",
            "Aging inventory risk"
        ]
    
    def get_financial_summary(self, inventory_data):
        """Generate executive-level financial analysis"""
        # TODO: Implement with actual logic
        return "Inventory Health: Total capital tied up $2.3M. Average turn: 24 days. Gross margin: 14.2%."
