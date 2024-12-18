from app.repositories.fix_info_repository import FixInfoRepository


async def get_all_fixes():
    fixes = await FixInfoRepository.get_all()

    return fixes


async def get_by_fix_id(fix_info_id: int):
    fix_info = await FixInfoRepository.get_by_id(fix_info_id)

    return fix_info

