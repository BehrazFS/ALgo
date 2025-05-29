# Algorithm-Design-Project

## 📌 Project Overview

This repository contains the implementation of a **three-phase individual project** for the Design and Analysis of Algorithms course. Each phase focuses on a different real-world optimization or data structure problem, requiring the design of efficient algorithms and data management systems.


## 🚀 Phase 1 – Minimum Cost University Network

* **Objective**: Connect all universities under the Ministry of Science using the minimum possible cost.
* **Input**: A complete directed graph in the form of a 2D matrix representing communication costs.
* **Goals**:

  * Ensure every university can connect to any other (directly or via intermediates).
  * Limit the maximum number of intermediate universities per communication to **2** (bonus).
  * Efficiently handle the addition of a new university (bonus).

🔧 **Algorithm Used**: Variants of **MST (Minimum Spanning Tree)** and **Graph Traversal with Constraints**


## 📂 Phase 2 – Student Information System

* **Objective**: Design an efficient system for storing and retrieving student data across multiple universities.
* **Features**:

  * Lookup student information in **O(log n)** time.
  * Determine the university of a student in **O(log m)** time.
  * Add a student or university in **O(1)** time.
  * Research Team Formation: Suggest top 5 students based on:

    * Topic similarity
    * Same major (priority)
    * GPA closeness
    * Bonus if they’re from the same university

🔧 **Data Structures Used**: **Binary Search Trees, Hash Maps, Heaps**


## 💰 Phase 3 – Internal University Optimization

### 🧠 Problem 1: Revenue Maximization

* **Scenario**: Each university has a monthly budget and investment options with varying returns and holding times.
* **Goal**: Maximize profit over `n` months using dynamic programming.
* **Choices**:

  1. Hold cash (no change).
  2. Educational workshops (1-month lock).
  3. Agricultural markets (6-month lock).

🔧 **Technique**: **Dynamic Programming (DP)**
🕒 **Bonus**: Optimize to **O(n)** time.


### 🎓 Problem 2: Class Scheduling Optimization

* **Scenario**: A student selects courses to maximize total units without time overlap.
* **Input**: List of courses with unit count, time range, and day.
* **Bonus**:

  * Handle online classes that may overlap in time but not in exam date.

🔧 **Technique**: **Weighted Interval Scheduling / Greedy Optimization**


## 🛠️ Technologies Used

* Language: `Python` / `C++` / `Java` (based on your implementation)
* Data Structures: Trees, Hash Tables, Priority Queues
* Algorithms: MST, DP, Greedy, Scheduling





final project of Design and Analysis of Algorithms cource
