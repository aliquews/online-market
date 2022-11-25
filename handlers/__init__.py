from aiogram import Router


def setup_routers() -> Router:
    from .admin import adminpanel, append_product, delete_product
    from .user import start, open_market, select_product

    router = Router()
    router.include_router(start.router)

    router.include_router(adminpanel.router)
    router.include_router(append_product.router)
    router.include_router(delete_product.router)

    router.include_router(open_market.router)
    router.include_router(select_product.router)

    return router
