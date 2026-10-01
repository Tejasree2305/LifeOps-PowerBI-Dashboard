# LifeOps -- Project Documentation

## 1. Project Overview

**LifeOps** is a Personal Productivity & Lifestyle Analytics project
developed to analyze multiple areas of day-to-day activity in one
interactive Power BI solution.

The project covers:

-   Daily activity and productivity
-   Tasks
-   Learning
-   Expenses
-   Goals
-   Habits
-   User-level analysis

The final Power BI report contains a landing page followed by analytical
pages for Overview, Tasks, Learning, Expenses, Goals, and Habits.

------------------------------------------------------------------------

## 2. Project Objective

The objective of LifeOps is to transform multi-domain lifestyle and
productivity data into an interactive analytical dashboard that helps
users understand:

-   Task workload and completion
-   Estimated versus actual task effort
-   Learning activity and assessment performance
-   Expense distribution and monthly spending
-   Goal progress and completion
-   Habit consistency and completion
-   Study and work patterns over time

------------------------------------------------------------------------

## 3. Technology Stack

  Technology    Purpose
  ------------- -------------------------------------------------------
  Python        Synthetic dataset generation
  CSV           Raw and processed data storage
  Excel         Dataset exploration/analysis
  SQL           Querying and analytical practice
  Power Query   Data cleaning and transformation
  Power BI      Data modeling and dashboard development
  DAX           KPI and analytical measure creation
  GitHub        Versioning, documentation, and portfolio presentation

------------------------------------------------------------------------

## 4. Dataset Generation

The project uses synthetic data generated with Python scripts.

The supplied generators create data for **200 users** and include:

  Dataset           Approximate Records Purpose
  --------------- --------------------- -------------------------------------------
  Users                             200 User attributes
  DailyActivity                  73,000 Daily productivity and lifestyle activity
  Tasks                          15,000 Task planning and completion
  Expenses                       20,000 Income/expense transactions
  Goals                           3,000 Personal and professional goals
  Learning                       10,000 Learning activity and performance
  Habits                         30,000 Habit tracking and completion

The use of synthetic data makes the project suitable for portfolio
demonstration without exposing real personal information.

------------------------------------------------------------------------

## 5. Data Dictionary

### Users

  Column       Description
  ------------ -------------------------
  UserID       Unique user identifier
  UserName     User name
  AgeGroup     User age-group category
  Occupation   User occupation
  City         User city

### DailyActivity

  Column              Description
  ------------------- ------------------------------
  ActivityID          Unique activity record
  UserID              Related user
  ActivityDate        Activity date
  StudyHours          Hours spent studying
  WorkHours           Hours spent working
  DeepWorkHours       Focused/deep-work hours
  MeetingHours        Hours spent in meetings
  ExerciseHours       Exercise duration
  LeisureHours        Leisure duration
  SleepHours          Sleep duration
  ProductivityScore   Generated productivity score

### Tasks

  Column           Description
  ---------------- --------------------------------------------------------
  TaskID           Unique task identifier
  UserID           Related user
  TaskDate         Task creation/activity date
  TaskCategory     Work, Learning, Personal, Health, Finance, or Project
  Priority         Low, Medium, High, or Critical
  TaskStatus       Completed, Pending, In Progress, Cancelled, or Overdue
  DueDate          Task due date
  CompletionDate   Date task was completed
  EstimatedHours   Estimated effort
  ActualHours      Actual effort
  IsOverdue        Overdue indicator

### Expenses

  Column            Description
  ----------------- -----------------------------------
  TransactionID     Unique transaction identifier
  UserID            Related user
  TransactionDate   Transaction date
  TransactionType   Income or Expense
  Category          Transaction category
  SubCategory       Detailed transaction category
  Amount            Transaction amount
  PaymentMethod     Payment method
  IsRecurring       Recurring transaction indicator
  IsEssential       Essential/non-essential indicator

### Goals

  -----------------------------------------------------------------------
  Column                              Description
  ----------------------------------- -----------------------------------
  GoalID                              Unique goal identifier

  UserID                              Related user

  GoalDate                            Goal creation date

  GoalType                            Financial, Health, Learning,
                                      Career, Personal, or Productivity

  GoalName                            Goal description

  Priority                            Goal priority

  TargetValue                         Target value

  CurrentValue                        Current progress value

  Deadline                            Goal deadline

  GoalStatus                          Goal status
  -----------------------------------------------------------------------

### Learning

  Column              Description
  ------------------- -------------------------------------
  LearningID          Unique learning record
  UserID              Related user
  LearningDate        Learning date
  Skill               Skill being learned
  CourseType          Learning format
  HoursSpent          Learning hours
  AssessmentScore     Assessment score
  CompletionPercent   Course/activity completion
  LearningStatus      Learning status
  DifficultyLevel     Beginner, Intermediate, or Advanced

### Habits

  Column             Description
  ------------------ -------------------------------
  HabitID            Unique habit record
  UserID             Related user
  HabitDate          Habit date
  HabitName          Habit being tracked
  HabitCategory      Habit category
  TargetValue        Target for the habit
  ActualValue        Actual achieved value
  CompletionStatus   Completed, Partial, or Missed
  StreakDays         Habit streak

------------------------------------------------------------------------

## 6. Data Preparation and Transformation

The project workflow separates source data from cleaned/processed data.

Recommended repository organization:

``` text
data/
├── raw/
│   ├── Users.csv
│   ├── DailyActivity.csv
│   ├── Tasks.csv
│   ├── Expenses.csv
│   ├── Goals.csv
│   ├── Learning.csv
│   └── Habits.csv
└── processed/
    ├── Tasks_Cleaned.csv
    ├── Learning_Cleaned.csv
    └── Habits_Cleaned.csv
```

If the current processed files are named `Tasks1.csv`,
`Learning_fixed.csv`, and `Habits_fixed.csv`, rename them to the clearer
names above before publishing, provided they are in fact the cleaned
versions used by the report.

Power Query is used in the Power BI workflow for data preparation,
data-type handling, and transformation before reporting.

------------------------------------------------------------------------

## 7. Data Model

The analytical model is centered around user and date dimensions with
subject-area tables for:

-   DailyActivity
-   Tasks
-   Expenses
-   Goals
-   Learning
-   Habits

A Date table is used for time-based analysis.

### Add a Model Screenshot

Place a screenshot exported/captured from **Power BI → Model View** in
this folder with the name:

``` text
data-model.png
```

This is useful for recruiters because it visually demonstrates the
relationships and modeling structure used in the project.

------------------------------------------------------------------------

## 8. DAX Measures

The project uses DAX measures to create dynamic KPIs.

### Example: Task Completion %

``` dax
Task Completion % =
DIVIDE(
    [Completed Tasks],
    [Total Tasks],
    0
)
```

The result should be formatted as a percentage.

### Recommended Measures to Document

Add the exact DAX from the final PBIX for the measures actually used in
the report, such as:

-   Total Tasks
-   Completed Tasks
-   Pending Tasks
-   Task Completion %
-   Total Learning Hours
-   Assessment/Completion measures
-   Total Expenses
-   Essential Expenses
-   Non-Essential Expenses
-   Total Goals
-   Completed Goals
-   Goal Completion %
-   Total Habits
-   Completed Habits
-   Habit Completion %

> Important: Only document formulas that are actually used in the final
> Power BI model. Do not add measures solely for GitHub documentation.

------------------------------------------------------------------------

## 9. Dashboard Pages

### Landing Page

Provides a branded entry point to the LifeOps report and navigation into
the analytical dashboard.

### Overview

Provides a high-level view of the LifeOps data through KPIs and summary
visualizations, including study versus work activity, expenses by
category, task status, and interactive filters.

### Tasks

Analyzes task workload and performance using task counts, completion
metrics, task status, and estimated-versus-actual effort comparisons.

### Learning

Analyzes learning hours, assessment performance, completion, learning
status, skills, and learning trends.

### Expenses

Analyzes spending behavior through total expenses, transaction-related
metrics, categories, essential/non-essential spending, and monthly
patterns.

### Goals

Tracks goal volume, completion, status, category/type, and progress
toward targets.

### Habits

Tracks habit activity, actual-versus-target performance, completion,
consistency, and trends over time.

------------------------------------------------------------------------

## 10. Dashboard Interactivity

The Power BI report includes interactive elements such as:

-   Page navigation
-   User filtering
-   Month/time filtering
-   Cross-filtering between visuals
-   KPI cards
-   Category/status comparisons
-   Trend analysis
-   Estimated-versus-actual comparisons

------------------------------------------------------------------------

## 11. Project Workflow

``` text
Python Data Generation
        ↓
CSV Datasets
        ↓
Excel / SQL Analysis
        ↓
Power Query Cleaning & Transformation
        ↓
Power BI Data Model
        ↓
DAX Measures
        ↓
Interactive Dashboard
        ↓
Analysis & Insights
```

------------------------------------------------------------------------

## 12. Skills Demonstrated

-   Power BI
-   Power Query
-   DAX
-   Data Modeling
-   Data Cleaning
-   Data Visualization
-   Dashboard Design
-   KPI Development
-   SQL
-   Excel
-   Python
-   Analytical Thinking

------------------------------------------------------------------------

## 13. Suggested Documentation Folder

Keep the folder simple:

``` text
documentation/
├── PROJECT_DOCUMENTATION.md
└── data-model.png
```

The `PROJECT_DOCUMENTATION.md` file contains the technical
documentation. `data-model.png` should be a clean screenshot of the
final Power BI Model View.

If desired later, the documentation can be split into separate files
such as `dax-measures.md` and `data-dictionary.md`, but that is not
necessary for a fresher portfolio repository.

------------------------------------------------------------------------

## 14. Notes for GitHub

-   Keep the final `.pbix` file under a `powerbi/` folder.
-   Keep Python generation scripts under `scripts/`.
-   Keep SQL under `sql/`.
-   Keep the Excel workbook under `excel/`.
-   Keep dashboard screenshots under `screenshots/`.
-   Keep the main `README.md` in the repository root.
-   Use clear filenames and avoid version names such as `(7)`, `fixed`,
    or `1` in the final published repository where possible.
-   State clearly in the README that the project uses
    **synthetic/generated data**.
