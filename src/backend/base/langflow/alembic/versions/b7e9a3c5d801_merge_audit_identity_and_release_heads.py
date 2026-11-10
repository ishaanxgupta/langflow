"""Merge represented audit identity and release migration heads.

Revision ID: b7e9a3c5d801
Revises: 7fd2c80e5a39, f6a2c8e4b901
Create Date: 2026-11-10

Phase: EXPAND

Join both migration histories without changing their revisions or stored data.
"""

from collections.abc import Sequence

revision: str = "b7e9a3c5d801"  # pragma: allowlist secret
down_revision: str | Sequence[str] | None = ("7fd2c80e5a39", "f6a2c8e4b901")  # pragma: allowlist secret
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
