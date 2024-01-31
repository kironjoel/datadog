# Python script to query and report the available Windows Updates using Dogstatsd
# This script sends the metric to the local DogStatsD agent. Datadog Agent must be installed on the system for this script to work.
# File location on system: C:\ProgramData\Datadog\checks.d\custom_windows_updates.py
# Script tested with Datadog Agent versions 7.45.1 and above

# Version: 1.0.0

from datadog_checks.base import AgentCheck
import psutil
import subprocess
import re
import platform

__version__ = "1.0.0"

class CustomWindowsUpdatesCheck(AgentCheck):

    def check(self, instance):
        updates_count = self.get_windows_updates_count()

        if updates_count is not None:
            # Send the metric to Datadog
            self.gauge('custom.windows.updates.available', updates_count)

    def get_windows_updates_count(self):
        try:
            if platform.system() == 'Windows':
                # Run PowerShell command to get the number of available updates
                command = 'powershell "Get-HotFix | Where-Object {$_.Description -like \'*Update\'} | Measure-Object | Select-Object -ExpandProperty Count"'
                result = subprocess.check_output(command, shell=True, text=True)

                # Convert the result to an integer
                updates_count = int(result.strip())
                return updates_count
            else:
                self.log.warning("This script is intended for Windows systems only.")
                return None
        except Exception as e:
            self.log.error(f"Error: {e}")
            return None