# Field-Rigging-Planning-Application
ProQee - an AI-powered application developed to support topside rigging design for oil and gas field construction projects, as well as operations and maintenance activities.

Developer: Celestine Iwomi. ProQee brings together my many years of hands-on construction engineering experience with my recent software development training to create practical innovations that improve safety, accuracy, and efficiency in the execution of oil and gas construction projects.

1.0	Overview
ProQee is a desktop-first rigging planning application designed to support engineers in the systematic development, verification, and documentation of lifting and rigging plans. It focuses on engineering accuracy, regulatory compliance, and traceability, providing a structured alternative to spreadsheets and fragmented CAD-based workflows.
ProQee is intentionally built with an engineering-first architecture: deterministic calculations, auditable data storage, and a clear separation between the user interface and the calculation logic. The system is designed to operate offline while remaining scalable for future collaboration, AI assistance, and enterprise deployment.

2.0	Key Objectives
•	Reduce rigging calculation errors through structured, validated workflows
•	Improve consistency in lift planning and documentation
•	Provide clear traceability from inputs to engineering results
•	Support compliance with lifting standards
•	Create a foundation for future intelligent optimisation and analytics 

3.0	Current Scope 
The Minimum Viable Product (MVP) of ProQee delivers a complete, end-to-end rigging planning workflow that combines a deterministic engineering core with targeted AI assistance. The MVP is designed to be usable in real engineering environments while laying the foundation for advanced automation and analytics.
3.1 Included in MVP 
•	Desktop application shell (Electron)
•	Engineering-focused UI (React + Typescript)
•	Certified gear library and compatibility validation 
•	Lift configuration and geometry definition 
•	Deterministic engineering calculations 
•	Compliance checks with explicit code references
•	Offline-first local database
•	AI-assisted optimisation for rigging configurations
•	3D visualisation and reconstruction for lift context
3.2 Deferred Beyond MVP
•	Large-scale multi-user cloud collaboration
•	AI-assisted optimisation
•	Computer vision and 3D reconstruction 
•	Real-time vendor integrations Cloud-only workflows

4.0 Core Features
4.1 AI-Enabled Capabilities 
•	AI-assisted optimisation of rigging arrangements to reduce over-specification while maintaining safety margins
•	Pattern-based recommendation support for visual site assessment using images to identify clearances, obstructions, and visible defects
•	3D reconstruction of lift environments for enhanced understanding and validation
4.2 Project Management
•	Structured project setup
•	Installation Planning (design, testing, mobilisation, etc)
•	Document status control (draft, checked, approved)
4.3 Gear Library
•	Certified rigging components
•	Filtered selection by capacity, material, and status
•	Explicit lift-gear mapping
•	Certificate traceability
4.4	Lift Configuration 
•	Definition of load weight and centre of gravity
•	Sling geometry and angles
•	Visual lift arrangement
•	Real-time validation feedback
4.5	Engineering Calculations
•	Static lift and sling tension calculations
•	Dynamic amplification factor support
•	Utilisation checks against gear WLL
•	Fully traceable formula outputs
4.6	Compliance and Warnings
•	Rule-based validation against governing codes
•	Clear warning levels (green/amber/red)
•	Code references attached to each warning
4.7	Reporting
•	Professional engineering reports
•	Calculation summaries and assumptions
•	Gear lists and certification references

5.0 Architecture Summary
Modular and layered architecture: 
•	Frontend: Electron + React (Typescript)
•	Engineering Core: Python (NumPy/SciPy)
•	Database: PostgreSQL(local-first)
•	Interface: Secure IPC/APC boundary between UI and calculations

6.0 Target Users 
•	Installation/construction engineers (installation/construction methods planning and reviews, including safety risk assessment)
•	Rigging engineers and lifting specialists
•	Field operation, maintenance and project teams
•	Procurement planning (lifting gears, accessories)

