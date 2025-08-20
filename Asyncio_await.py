import asyncio
import time

async def fetch_user_info(user_id) -> dict:
    print(f"Begin get user info from database with user id: {user_id}")
    await asyncio.sleep(2)
    print(f"just given info of user {user_id}")
    return {"id": user_id, "username": "Xavie Le", "email": "user1@gmail.com"}

async def fetch_user_order(user_id) -> list:
    print(f"give order of user {user_id}")
    await asyncio.sleep(2)
    print(f"given order data of user {user_id} successfully")
    return [{"order_id": 1, "total": 100}, {"order_id": 2, "total": 200}]
async def main():
    user_id = 123
    start_time = time.time()

    user_data_concurrent, order_data_concurrent = await asyncio.gather(
        fetch_user_info(user_id),
        fetch_user_order(user_id)
    )

    print(f"user data: {user_data_concurrent}")
    print(f"order data: {order_data_concurrent}")
if __name__ == "__main__":
    asyncio.run(main())