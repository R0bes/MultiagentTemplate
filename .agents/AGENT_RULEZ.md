# AGENT_RULEZ 🚀

## Die Regeln für unser Multi-Agent-System

### 🎯 Übersicht
Alle Agents folgen diesen Regeln. Punkt. Keine Ausnahmen. Das ist unser Code of Conduct für kollaborative AI-Projekte.

---

## 🏗️ Agent-Rollen & Verantwortlichkeiten

### 🎯 Meta Agent (Agent Queen)
- **Was macht er**: Projektkoordination und Workflow-Management
- **Fokus**: Workflow orchestrieren, Fortschritt überwachen, Probleme lösen

### 🏗️ Architect Agent
- **Was macht er**: Systemdesign und Architekturplanung
- **Fokus**: "Was" muss gebaut werden, nicht "wie"

### 🧪 Tester Agent
- **Was macht er**: Umfassende Test-Suites erstellen
- **Fokus**: Contract-basiertes Testing, Coverage-Analyse

### 💻 Solver Agent
- **Was macht er**: Funktionalität nach Contract implementieren
- **Fokus**: Contract-Compliance, Code-Qualität

### ⚖️ Judge Agent
- **Was macht er**: CI-Ausführung und Qualitätsvalidierung
- **Fokus**: Test-Ausführung, Quality Gates, redigiertes Feedback

---

## 📋 Wesentliche Arbeitsregeln

### Task-Lifecycle
Alle Agents müssen:
1. **Tasks aus der Inbox holen** (`msg/inbox/`)
2. **In Running kopieren** (`msg/running/`)
3. **Bearbeiten und in Done verschieben** (`msg/done/`) oder bei Fehlern in `msg/failed/`


### Healthcheck
- **Alle 2-3 Minuten**
- Status und Fortschritt melden


### Task-Zeitlimit
- **Tasks dürfen nicht länger als 3 Minuten dauern**
- **Aufwand zu Beginn schätzen**
- **Bei >3 Minuten**: Task in zwei Teile aufteilen (falls möglich)
- **Falls nicht teilbar**: Warnung ausgeben


### Reporting
- **Alle Agents müssen kontinuierlich reporten**
- Nach jeder Aktion Status aktualisieren
- Fortschritt dokumentieren


## 🔐 Verzeichnisstruktur
Jeder Agent hat folgende Verzeichnisstruktur:
- `msg/inbox/` - Eingehende Nachrichten
- `msg/running/` - Laufende Aufgaben
- `msg/done/` - Abgeschlossene Aufgaben
- `msg/failed/` - Fehlgeschlagene Aufgaben


### Ausgabeformat für andere Agenten

## Task-Template verwenden
Alle Tasks müssen dem Template folgen:
{{#include ../../templates/task.yml}}


## 🚦 Quality Gates
- **Coverage**: Mindestens 85% Testabdeckung
- **Linting**: Alle Regeln müssen passieren
- **Performance**: Alle Limits einhalten


**AGENT_RULEZ** - Weil Regeln sind Regeln! 🚀⚡
