#!/usr/bin/env python3
"""
Einfaches Skript zum Leeren aller .agents/roles/*/msg/*/ und src/ Verzeichnisse
"""

import shutil
from pathlib import Path

def main():
    print("🧹 Leere Verzeichnisse...")
    
    # Alle msg Verzeichnisse leeren
    for msg_dir in Path(".agents").rglob("msg"):
        for subdir in ["inbox", "running", "done", "failed"]:
            target = msg_dir / subdir
            if target.exists():
                shutil.rmtree(target)
                target.mkdir()
                print(f"✅ {target} geleert")
    
    # src Verzeichnis leeren
    src = Path("src")
    if src.exists():
        shutil.rmtree(src)
    src.mkdir(exist_ok=True)
    print("✅ src/ geleert")
    
    print("🎉 Fertig!")

if __name__ == "__main__":
    main()
