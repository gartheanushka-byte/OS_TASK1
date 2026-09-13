# OS_TASK1
# Operating Systems – Task 1

## Multithreading Implementation of Producer–Consumer and Matrix Multiplication Visualization

This project demonstrates fundamental **Operating Systems multithreading concepts** through two implementations:

1. **Producer–Consumer Problem** using Python threads and a bounded queue.
2. **Matrix Multiplication** using Python multithreading along with a browser-based visualization.

---

## 📌 Objectives

* Understand the concept of multithreading.
* Create and manage multiple threads using Python.
* Implement the Producer–Consumer model.
* Use a bounded `Queue` for thread synchronization.
* Understand `put()`, `get()`, `task_done()`, `start()`, and `join()`.
* Implement matrix multiplication using multiple threads.
* Compare the concept of sequential and threaded matrix multiplication.
* Visualize independent matrix multiplication contributions using HTML, CSS, and JavaScript.

---

## 🛠️ Technologies Used

* **Python 3**
* Python `threading` module
* Python `queue` module
* Python `time` module
* HTML5
* CSS3
* JavaScript

---

# 1. Producer–Consumer Implementation

The first program demonstrates the **Producer–Consumer model** using Python multithreading.

A bounded queue with a capacity of **3** is used as the shared mailbox. One thread produces five items, while another thread consumes them.

### Working

* Producer thread inserts numbers `1` to `5`.
* Consumer thread removes the items from the queue.
* The queue has a maximum capacity of `3`.
* `task_done()` marks each consumed item as completed.
* `start()` starts the threads.
* `join()` ensures that the main thread waits for both threads to finish.

### Program Structure

```text
Main Thread
    │
    ├── Writer / Producer Thread
    │       └── Produces 1, 2, 3, 4, 5
    │
    └── Reader / Consumer Thread
            └── Consumes 1, 2, 3, 4, 5
                    │
                    ▼
              Bounded Queue
              Capacity = 3
```

### Execution

Run the Python program:

```bash
python producer_consumer.py
```

Example output:

```text
[Producer] placed item 1
[Consumer] removed item 1
[Producer] placed item 2
[Consumer] removed item 2
...
Both threads completed their work.
```

The exact order and timing of messages may vary because thread execution depends on scheduling.

---

# 2. Threaded Matrix Multiplication

The second Python implementation performs matrix multiplication using multiple threads.

The program:

* Generates two random `100 × 100` matrices.
* Calculates the expected result using sequential multiplication.
* Creates a separate thread for each matrix row.
* Each thread calculates one row of the result matrix.
* Uses `join()` to wait for all worker threads.
* Measures execution time using `time.perf_counter()`.
* Verifies whether the threaded result matches the sequential result.

For each result element:

```text
C[i][j] = Σ A[i][k] × B[k][j]
```

### Threading Approach

```text
Matrix A        Matrix B
   │               │
   └───────┬───────┘
           ▼
    Matrix Multiplication
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
 Thread  Thread  Thread
   Row 0   Row 1   Row 2 ...
     │     │     │
     └─────┼─────┘
           ▼
       Matrix C
```

The implementation creates **100 worker threads**, with each thread responsible for calculating one row of the result matrix.

### Execution

```bash
python matrix_multiplication.py
```

Example output:

```text
Loading matrices into RAM...
Matrices loaded successfully.

Threaded matrix multiplication finished.
Matrix size: 100 x 100
Worker threads created: 100
Elapsed time: X.XXXX seconds
Threaded result is correct: True
Sample result [0][0]: XXXXX
```

---

# 3. Matrix Multiplication Visualization

A browser-based visualization named **Threaded Matrix Laboratory** is also included.

It provides a visual representation of independent matrix multiplication contributions.

The interface contains:

* Input Matrix A
* Input Matrix B
* Output Matrix
* Worker contribution indicator
* Processing status
* CSS animations

The visualization uses **5 × 5 grids** and dynamically generates values between `1` and `9`.

### Important Note

The HTML visualization is an **educational visualization**. It does not create actual operating-system threads or Web Workers in the browser. Instead, JavaScript periodically displays matrix multiplication contribution concepts such as:

```text
A[row][k] × B[k][column]
```

The actual threaded matrix multiplication is implemented separately in Python.

---

## 📂 Project Structure

```text
OS-TASK-1/
│
├── README.md
│
├── producer_consumer.py
│
├── matrix_multiplication.py
│
└── threaded_matrix_lab.html
```

---

## ▶️ How to Run

### Prerequisites

Install **Python 3** on your system.

Check the installation:

```bash
python --version
```

### Run Producer–Consumer

```bash
python producer_consumer.py
```

### Run Matrix Multiplication

```bash
python matrix_multiplication.py
```

### Run Visualization

Open:

```text
threaded_matrix_lab.html
```

in any modern web browser.

---

## 🔑 Key Concepts Demonstrated

| Concept                 | Implementation             |
| ----------------------- | -------------------------- |
| Multithreading          | Python `threading`         |
| Producer–Consumer       | Python                     |
| Synchronization         | `queue.Queue`              |
| Bounded Buffer          | Queue capacity = 3         |
| Thread Creation         | `threading.Thread()`       |
| Thread Start            | `start()`                  |
| Thread Synchronization  | `join()`                   |
| Queue Completion        | `task_done()`              |
| Matrix Multiplication   | Python                     |
| Parallel Row Processing | One thread per row         |
| Execution Time          | `time.perf_counter()`      |
| Visualization           | HTML, CSS, JavaScript      |
| Animation               | CSS Keyframes + JavaScript |

---

## ✅ Advantages

### Producer–Consumer

* Simple and easy to understand.
* Uses a synchronized bounded queue.
* Separates producing and consuming tasks.
* Demonstrates thread lifecycle management.
* Shows coordination between concurrent activities.

### Matrix Multiplication

* Demonstrates parallel row-wise computation.
* Uses multiple worker threads.
* Verifies threaded output against sequential output.
* Measures execution time.
* Provides a visual representation of matrix computation.

---

## ⚠️ Limitations

* Producer–Consumer uses only one producer and one consumer.
* The producer and consumer process a fixed number of five items.
* The matrix visualization is conceptual and does not perform actual browser multithreading.
* The visualization does not calculate a complete matrix product.
* The Python matrix implementation is primarily intended to demonstrate multithreaded computation rather than optimized production performance.

---

## 📚 Learning Outcomes

Through this task, the following concepts were explored:

* Basic purpose of threads within a process.
* Thread creation and lifecycle management.
* Producer–Consumer synchronization.
* Bounded queues and blocking operations.
* Use of `put()`, `get()`, and `task_done()`.
* Use of `start()` and `join()`.
* Effects of timing and scheduling on concurrent execution.
* Decomposition of matrix multiplication into independent tasks.
* Difference between actual Python multithreading and browser-based visualization.

---

## 📖 References

1. Python Documentation – `threading` module
2. Python Documentation – `queue` module
3. Abraham Silberschatz, Peter B. Galvin and Greg Gagne – *Operating System Concepts*
4. Andrew S. Tanenbaum and Herbert Bos – *Modern Operating Systems*
5. Operating Systems course notes and laboratory material
