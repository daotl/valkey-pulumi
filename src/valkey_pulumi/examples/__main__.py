"""Run Valkey example deployments with Pulumi.

Select an example by setting VALKEY_EXAMPLE to one of:
  - standalone (default)
  - replica_set
  - tls
  - acl
"""

import os
import sys

# Ensure parent directory is in python path to allow imports
# This is needed if this file is run directly or via Pulumi from a different working directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from valkey_pulumi.examples.acl_example import deploy_acl_valkey
from valkey_pulumi.examples.replica_set import deploy_valkey_replica_set
from valkey_pulumi.examples.standalone import deploy_standalone_valkey
from valkey_pulumi.examples.tls_example import deploy_tls_valkey


def main():
    """Run the selected Valkey deployment example.

    Reads the VALKEY_EXAMPLE environment variable to determine which example
    to run. Defaults to 'standalone' if not set.

    Available examples:
        - standalone: Deploys a single Valkey instance
        - replica_set: Deploys Valkey with replica configuration
        - tls: Deploys Valkey with TLS encryption
        - acl: Deploys Valkey with Access Control Lists (ACL)

    Returns:
        None

    Raises:
        ValueError: If VALKEY_EXAMPLE is set to an unsupported value.

    """
    choice = os.environ.get("VALKEY_EXAMPLE", "standalone").lower()

    if choice == "replica_set":
        deploy_valkey_replica_set()
    elif choice == "tls":
        deploy_tls_valkey()
    elif choice == "acl":
        deploy_acl_valkey()
    else:
        deploy_standalone_valkey()


if __name__ == "__main__":
    main()
