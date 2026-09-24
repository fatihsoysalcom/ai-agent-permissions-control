import json

# Simulate a user's permissions
user_permissions = {
    "read_customer_data": True,
    "update_inventory": False,
    "process_payments": False,
    "send_notifications": True
}

# Simulate an AI agent's requested permissions
# This agent has more permissions than the user
ai_agent_requested_permissions = {
    "read_customer_data": True,
    "update_inventory": True,
    "process_payments": True,
    "send_notifications": True,
    "access_financial_records": True
}

def check_permission(permissions, permission_name):
    """Checks if a specific permission is granted."""
    return permissions.get(permission_name, False)

def enforce_least_privilege(user_perms, agent_req_perms):
    """Enforces the principle of least privilege for the AI agent."""
    granted_agent_permissions = {}
    for perm, required in agent_req_perms.items():
        # Grant permission only if the user also has it, or if it's a generally safe permission
        # In a real system, this logic would be more sophisticated, involving roles and policies.
        if user_perms.get(perm, False) or not required: # Simplified: If user has it, grant. If not required by agent, grant (for demo).
            granted_agent_permissions[perm] = True
        else:
            granted_agent_permissions[perm] = False
    return granted_agent_permissions

print("--- User Permissions ---")
print(json.dumps(user_permissions, indent=2))

print("\n--- AI Agent Requested Permissions ---")
print(json.dumps(ai_agent_requested_permissions, indent=2))

# Demonstrate the risk: Agent directly using its requested permissions (if unchecked)
print("\n--- Direct Agent Access (RISK EXAMPLE) ---")
if check_permission(ai_agent_requested_permissions, "access_financial_records"):
    print("AI Agent can access financial records (UNSAFE if not properly managed).")
else:
    print("AI Agent cannot access financial records.")

# Apply least privilege principle
print("\n--- AI Agent Permissions After Least Privilege Enforcement ---")
final_agent_permissions = enforce_least_privilege(user_permissions, ai_agent_requested_permissions)
print(json.dumps(final_agent_permissions, indent=2))

# Demonstrate the solution: Agent using enforced permissions
print("\n--- Agent Access After Enforcement (SAFE) ---")
if check_permission(final_agent_permissions, "access_financial_records"):
    print("AI Agent can access financial records.")
else:
    print("AI Agent cannot access financial records (as intended by least privilege).")

if check_permission(final_agent_permissions, "update_inventory"):
    print("AI Agent can update inventory.")
else:
    print("AI Agent cannot update inventory (user does not have this permission).")
