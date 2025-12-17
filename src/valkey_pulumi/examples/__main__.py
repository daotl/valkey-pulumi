"""Run Valkey example deployments with Pulumi.

Select an example by setting VALKEY_EXAMPLE to one of:
  - standalone (default)
  - replica_set
  - tls
  - acl
"""

import os

from valkey_pulumi.examples.acl_example import acl_valkey
from valkey_pulumi.examples.replica_set import deploy_valkey_replica_set
from valkey_pulumi.examples.standalone import deploy_standalone_valkey
from valkey_pulumi.examples.tls_example import tls_valkey


def main():
    """
    Run the selected Valkey example based on the VALKEY_EXAMPLE environment variable.
    
    Reads VALKEY_EXAMPLE (defaults to "standalone") and deploys the corresponding example:
    - "standalone": deploys a single Valkey instance
    - "replica_set": deploys a replica-set configuration
    - "tls": triggers the TLS example (resources created at import time)
    - "acl": triggers the ACL example (resources created at import time)
    """
    choice = os.environ.get("VALKEY_EXAMPLE", "standalone").lower()

    if choice == "replica_set":
        deploy_valkey_replica_set()
    elif choice == "tls":
        # The TLS example instantiates resources at import-time; reference to keep lint happy
        _ = tls_valkey
    elif choice == "acl":
        _ = acl_valkey
    else:
        deploy_standalone_valkey()


if __name__ == "__main__":
    main()