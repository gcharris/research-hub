Here are the **copy-paste ready prompts** for the Personal Vital Signs Visualizer project, designed to demonstrate Anti-Gravity IDE's agentic workflow from start to finish.

## Prompt 1: Build the Base Medical Monitor

```
Create a Medical Vital Signs Monitor web app using React, TypeScript, and Recharts. 
The app should simulate a patient monitoring system with:

- Left sidebar: Patient selector with 5 mock patients (John Smith, 45; Maria Garcia, 32; David Chen, 58; Sarah Johnson, 28; Robert Williams, 67) showing age and patient ID
- Main dashboard: Real-time ECG waveform display (using animated LineChart with 500ms updates)
- Vital signs cards: Heart Rate (bpm), Blood Pressure (mmHg), Oxygen Saturation (%), Respiratory Rate (breaths/min)
- Color-coded alerts: Red for critical values (HR <60 or >100, SpO2 <95%), yellow for warning, green for normal
- Trend analysis: 24-hour line charts for each vital sign with time range selector (1h, 6h, 12h, 24h)
- Medical device aesthetic: Dark theme with teal accents, monospace fonts for numbers, grid lines like medical monitors

Use realistic physiological data ranges and make the ECG waveform look authentic with PQRST complexes.
```

**Expected Result**: Full working monitor with animated waveforms, selectable patients, and color-coded vital signs in 15-20 minutes [1][2].

## Prompt 2: Add Cardiac Arrhythmia Detection

```
Add a Cardiac Arrhythmia Detection panel below the ECG waveform. 
The panel should:
- Analyze the heart rate data in real-time and detect these conditions: Normal Sinus Rhythm, Tachycardia (HR >100), Bradycardia (HR <60), and Arrhythmia (irregular intervals)
- Display the current detected rhythm in large text with a confidence percentage (0-100%)
- Show a small history log of the last 10 rhythm detections with timestamps
- Use red highlighting for abnormal rhythms, green for normal
- Update the detection every 5 seconds based on the recent heart rate data
```

**Expected Result**: AI-powered cardiac analysis panel that demonstrates clinical decision support capabilities in 3-5 minutes [3].

## Prompt 3: Create Medication Tracker

```
Create a Medication Tracker section in the right sidebar that shows:
- Current medications for the selected patient with name, dosage, and frequency
- Next administration time countdown timer that updates every minute
- "Mark as Taken" button for each medication that logs the action
- When clicked, add the medication name and timestamp to a compliance log below
- Show medication adherence percentage for the past 7 days
- Use mock data: Aspirin 81mg daily, Lisinopril 10mg twice daily, Metformin 500mg with meals

Style it with medical-grade precision and clear visual hierarchy.
```

**Expected Result**: Interactive medication management system showing real-time compliance tracking in 3-5 minutes [4].

## Prompt 4: Implement Clinical Notes

```
Add a Clinical Notes feature at the bottom of the main dashboard:
- Text area where I can type observations for the selected patient
- "Add Note" button that saves the note with timestamp to local storage
- Display all notes in reverse chronological order below the text area
- Each note should show date, time, and note text in a clean card layout
- Add a search bar above the notes to filter by keyword
- Include a "Delete" button for each note with confirmation dialog

Make the notes persist when switching between patients and refreshing the page.
```

**Expected Result**: Full clinical documentation system with search and persistent storage in 3-5 minutes [2].

## Prompt 5: Refinement & Polish

```
The ECG waveform looks good but make these improvements:
- Add a subtle glow effect to the waveform line in teal color
- Increase the line thickness to 3px for better visibility
- Add grid lines that match medical monitor standards (light gray, 0.5px)
- Make the waveform container slightly taller (400px height)
- Add a small label "Lead II" at the top left of the waveform area
- Ensure the animation is smooth without any flickering

Also, make the vital signs cards larger and add subtle hover effects.
```

**Expected Result**: Professional-grade medical interface polish that demonstrates iterative refinement in 2-3 minutes [5].

## How to Use These Prompts

1. **Copy Prompt 1** into Anti-Gravity IDE and press Enter
2. Wait for the Agent Manager to create the plan, then click "Approve"
3. Watch the agents work in parallel while the browser preview updates in real-time
4. Once complete, **copy Prompt 2** and repeat the process
5. Continue through all prompts to build the complete system

Each prompt triggers the full agentic cycle: planning → execution → testing → deployment, showing your friend how natural language becomes working medical software [1][2].

