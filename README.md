# OLYMPUS
New SHED aka SHED 2023

https://www.noisebridge.net/wiki/Olympus

Proposed file project file structure:

```
Olympus/
├── src/
│   ├── db/
|   │   ├── __init__.py
│   |   └── json_database.py
│   ├── hardware/
│   |   ├── __init__.py
│   |   ├── door_sensor.py
│   |   ├── oled_display.py
│   |   ├── toggle_switch.py
│   |   └── rfid_scanner.py
│   ├── utils/
│   |   ├── __init__.py
│   |   ├── logger.py
│   |   ├── discord_notifier.py
│   └── olympus.py
├── tests/
│   ├── db/
|   │   ├── __init__.py
│   |   └── json_database_test.py
│   ├── hardware/
│   |   ├── __init__.py
│   |   ├── door_sensor_test.py
│   |   ├── test_oled_display_test.py
│   |   ├── test_rfid_scanner_test.py
│   |   └── test_toggle_switch_test.py
│   └── utils/
|       ├── __init__.py
│       ├── logger_test.py
│       └── discord_notifier_test.py
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── ...
├── .gitignore
├── README.md
├── LICENSE
├── setup.py
├── requirements.txt
├── MANIFEST.in
└── pyproject.toml

```