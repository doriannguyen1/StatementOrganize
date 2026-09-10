"""Utility functions for statement processing."""

def contains(haystack, needle):
    """Case-insensitive substring check. Returns False for None/empty inputs."""
    if not haystack or not needle:
        return False
    return needle.strip().lower() in haystack.strip().lower()
