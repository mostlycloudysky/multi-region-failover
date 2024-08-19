import unittest
import subprocess


class TestKinesisFailover(unittest.TestCase):

    def test_failover(self):
        result = subprocess.run(
            ["python", "kinesis/scripts/simulate_failover.py"],
            capture_output=True,
            text=True,
        )
        output = result.stdout

        # Check if the success messages are in the output
        self.assertIn("Success: Data sent to primary region.", output)
        self.assertIn("Success: Data sent to secondary region.", output)


if __name__ == "__main__":
    unittest.main()
