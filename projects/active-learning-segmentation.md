# Learning Which Images Need Expert Attention

**Context:** Master’s interdisciplinary project at FH Aachen  
**Application:** Turf-damage segmentation for TurfCare  
**Status:** In progress — implementation and experimental results pending  
**My focus:** Active-learning loop and query strategies

## The problem

Training an image-segmentation model requires labeled examples. For turf-damage segmentation, these labels identify the regions of an image that contain damage.

Creating these annotations takes expert time. This raises an important question:

**Can we train a useful segmentation model while asking experts to label fewer images?**

Our project explores active learning as a way to investigate this question.

## The idea

An active-learning workflow starts with a small labeled dataset and a larger pool of unlabeled images.

After training an initial model, the system selects additional images for annotation. The model is then retrained using the expanded labeled dataset.

The selection strategy determines which images receive expert attention. Our experiments will investigate whether targeted selection makes better use of the annotation budget than random selection.

## My planned contribution

My focus is the workflow connecting model predictions, image selection, annotation requests and retraining.

I plan to:

- Implement the active-learning loop in Python.
- Connect model predictions to image-selection strategies.
- Simulate expert annotation by revealing hidden dataset labels only after an image is selected.
- Compare selection strategies under a consistent annotation budget.
- Track segmentation performance and the number of labels used.
- Document experimental settings so comparisons can be reproduced.

## Planned selection strategies

### Random sampling

Select images randomly. This provides a baseline against which more targeted strategies can be compared.

### Entropy-based selection

Prioritize images based on uncertainty in the model’s predictions. The experiment will require a clear method for combining pixel-level uncertainty into an image-level score.

### BALD

Investigate selection based on disagreement across stochastic model predictions, where supported by the model and experimental setup.

### Core-set selection

Investigate selecting representative images that improve coverage of the dataset in a chosen feature space.

These methods are planned comparisons. Their implementation and suitability will be assessed during the project.

## How we plan to evaluate progress

The experiments will compare segmentation quality against the cumulative number of expert-labeled images.

The aim is to produce learning curves showing how each strategy performs as the annotation budget increases.

We plan to record experiment configurations, performance measures and annotation usage in MLflow. Final metrics and experimental settings will be agreed with the project team.

## How this builds on my experience

At FairVisit, I work on Python pipelines, data validation, background processing and automated tests.

This project extends that foundation into machine-learning experimentation. It gives me an opportunity to investigate how data selection influences model performance and how expert feedback can be incorporated into a repeatable workflow.

## Current stage

The project is ongoing. This page describes the problem, intended approach and my planned responsibilities.

Completed experiments, implementation details and measured results will be added as the work progresses.

## Publication note

Project code, images and datasets will be shared only where permission and licensing allow. No private project materials are included here.
