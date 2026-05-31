# Store Intelligence System Design

## Overview

This system processes CCTV footage to generate business metrics such as visitor count, entry/exit events, and store conversion metrics.

## Architecture

CCTV Video
↓
YOLOv8 Person Detection
↓
ByteTrack Person Tracking
↓
Entry/Exit Event Detection
↓
Event Storage (events.jsonl)
↓
FastAPI Analytics Layer
↓
Business Metrics API

## Components

### Detection Layer

YOLOv8 is used to detect people in CCTV frames.

### Tracking Layer

ByteTrack assigns persistent IDs to detected visitors.

### Event Generation

Line crossing logic generates ENTRY and EXIT events.

### Event Storage

Events are stored in JSONL format for simplicity and auditability.

### API Layer

FastAPI exposes business metrics through REST endpoints.

## Supported APIs

* /metrics
* /funnel
* /anomalies

## Assumptions

* CAM3 acts as entrance camera.
* Right-to-left crossing indicates entry.
* Left-to-right crossing indicates exit.
* One visitor is represented by one active tracking ID.
