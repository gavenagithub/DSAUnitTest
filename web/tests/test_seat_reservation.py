import unittest
import sys
import os
# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from upload.seat_reservation import find_seat, reserve_seat    
# where are the rest of the unittest code?
class TestSeatReservation(unittest.TestCase):
    def test_find_seat(self):
        seating_chart = [("1A", "Available"), ("1B", "Reserved"), ("2A", "Available")]
        self.assertEqual(find_seat(seating_chart, "1A"), "1A")
        self.assertEqual(find_seat(seating_chart, "Window"), "Not Available")
    def test_reserve_seat(self):
        seating_chart = [("1A", "Available"), ("1B", "Reserved"), ("2A", "Available")]
        seating_chart = reserve_seat(seating_chart, "1A")
        self.assertEqual(seating_chart, [("1A", "Reserved"), ("1B", "Reserved"), ("2A", "Available")])
        seating_chart = reserve_seat(seating_chart, "2A")
        self.assertEqual(seating_chart, [("1A", "Reserved"), ("1B", "Reserved"), ("2A", "Reserved")])

if __name__ == "__main__":
    unittest.main()