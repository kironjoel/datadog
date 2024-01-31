Datadog custom check to display available windows updates for a Windows Server. The metric is sent to Datadog as a custom metric custom.windows.updates.available

**Instructions**

Place the python script under C:\ProgramData\Datadog\checks.d and the yaml file under C:\ProgramData\Datadog\conf.d. Restart the Datadog Agent to start collecting this metric.

**Pre-requisite:**

Datadog Agent must be installed on the Windows Server.
