import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# async def configure_mongo_db(
#     mongo_db: MongoDatabase = Provide[Container.mongo_database],
# ):
#     async with mongo_db.session() as session:
#         await session.configure_database([Piece])


def create_app() -> FastAPI:
    app = FastAPI(openapi_url="/spec")

    # container = Container()

    from application.user import controller

    controller.configure(app)

    # container.wire(modules=[__name__, controller])

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)

    # loop.create_task(configure_mongo_db())
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.container = container
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
