create database LifeOpsDB;
go

use LifeOpsDB;

SELECT DB_NAME() AS CurrentDatabase;

CREATE TABLE Users
(
    UserID VARCHAR(10) PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    AgeGroup VARCHAR(20),
    Occupation VARCHAR(50),
    City VARCHAR(50)
);
SELECT * FROM Users;

CREATE TABLE DailyActivity
(
    ActivityID INT PRIMARY KEY,
    UserID VARCHAR(10) NOT NULL,
    ActivityDate DATE NOT NULL,
    StudyHours DECIMAL(5,2),
    WorkHours DECIMAL(5,2),
    DeepWorkHours DECIMAL(5,2),
    MeetingHours DECIMAL(5,2),
    ExerciseHours DECIMAL(5,2),
    LeisureHours DECIMAL(5,2),

    CONSTRAINT FK_DailyActivity_Users
    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)
);
SELECT * FROM DailyActivity;

CREATE TABLE Tasks
(
    TaskID INT PRIMARY KEY,
    UserID VARCHAR(10) NOT NULL,
    TaskDate DATE NOT NULL,
    Category VARCHAR(50),
    Priority VARCHAR(20),
    EstimatedHours DECIMAL(5,2),
    ActualHours DECIMAL(5,2),
    Status VARCHAR(20),

    CONSTRAINT FK_Tasks_Users
    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)
);
SELECT * FROM Tasks;

CREATE TABLE Expenses
(
    ExpenseID INT PRIMARY KEY,
    UserID VARCHAR(10) NOT NULL,
    ExpenseDate DATE NOT NULL,
    Category VARCHAR(50),
    Amount DECIMAL(10,2),
    PaymentMode VARCHAR(30),

    CONSTRAINT FK_Expenses_Users
    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)
);
SELECT * FROM Expenses;

CREATE TABLE Goals
(
    GoalID INT PRIMARY KEY,
    UserID VARCHAR(10) NOT NULL,
    GoalCategory VARCHAR(50),
    GoalName VARCHAR(100),
    TargetValue DECIMAL(10,2),
    CurrentValue DECIMAL(10,2),
    StartDate DATE,
    TargetDate DATE,
    Status VARCHAR(20),

    CONSTRAINT FK_Goals_Users
    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)
);
SELECT * FROM Goals;

CREATE TABLE Learning
(
    LearningID INT PRIMARY KEY,
    UserID VARCHAR(10) NOT NULL,
    LearningDate DATE NOT NULL,
    Skill VARCHAR(50),
    LearningHours DECIMAL(5,2),
    PracticeHours DECIMAL(5,2),
    AssessmentScore DECIMAL(5,2),

    CONSTRAINT FK_Learning_Users
    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)
);
SELECT * FROM Learning;

CREATE TABLE Habits
(
    HabitID INT PRIMARY KEY,
    UserID VARCHAR(10) NOT NULL,
    HabitDate DATE NOT NULL,
    HabitName VARCHAR(50),
    Completed BIT,

    CONSTRAINT FK_Habits_Users
    FOREIGN KEY (UserID)
    REFERENCES Users(UserID)
);
SELECT * FROM Habits;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_NAME;