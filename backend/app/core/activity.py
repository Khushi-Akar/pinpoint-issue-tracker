import uuid

from sqlmodel import Session

from app.models import IssueActivity


def log_activity(
    session: Session,
    issue_id: uuid.UUID,
    actor_id: uuid.UUID | None,
    action: str,
    detail: str | None = None,
) -> None:
    activity = IssueActivity(
        issue_id=issue_id,
        actor_id=actor_id,
        action=action,
        detail=detail,
    )
    session.add(activity)
