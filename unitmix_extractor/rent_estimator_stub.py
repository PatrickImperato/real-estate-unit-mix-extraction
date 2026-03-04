class RentEstimatorStub:
    def estimate_annual_rent(self, beds: int, baths, location_key: str) -> int:
        base = 12000
        bed_add = beds * 3500
        bath_add = int(float(baths) * 1500)
        loc_add = (sum(ord(c) for c in location_key) % 7) * 400
        return base + bed_add + bath_add + loc_add
