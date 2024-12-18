from fastapi import (
    HTTPException,
    Path,
    Body,
    Depends
)


from app.infrastructure.schemas.fix_info_schemas import SFixInfoUpdate
from app.repositories.fix_info_repository import FixInfoRepository


async def update_fix_by_id(fix_info_id: int = Path(...), request_body: SFixInfoUpdate = Body(...)):
    try:
        fix_data = request_body.model_dump(exclude_none=True)

        fix = await FixInfoRepository.update(
            {'fix_info_id': fix_info_id},
            **fix_data
        )

        if fix is None:
            raise HTTPException(status_code=404, detail="Fix not found")

        return fix
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))