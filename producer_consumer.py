import queue
import threading
import time

CAPACITY = 3
ITEM_COUNT = 5
mailbox = queue.Queue(maxsize=CAPACITY)


def fill_mailbox():
    for number in range(1, ITEM_COUNT + 1):
        mailbox.put(number)
        print(f"[Producer] placed item {number}")
        time.sleep(0.6)


def empty_mailbox():
    for _ in range(ITEM_COUNT):
        number = mailbox.get()
        print(f"[Consumer] removed item {number}")
        mailbox.task_done()
        time.sleep(1.0)


def main():
    writer = threading.Thread(target=fill_mailbox, name="writer")
    reader = threading.Thread(target=empty_mailbox, name="reader")

    writer.start()
    reader.start()

    writer.join()
    reader.join()

    print("Both threads completed their work.")


if __name__ == "__main__":
    main()
