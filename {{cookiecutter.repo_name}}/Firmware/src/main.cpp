/**
 * @file main.cpp
 * @author {{cookiecutter.author}}
 * @brief Source code for {{cookiecutter.repo_name}}
 */

// Libs
#include <Arduino.h>

// Headers
#include "boardPins.h"

void setup()
{
    // Setup serial
    delay(200);
    Serial.begin(115200);
    Serial.println(REVISION);

    // Pins
    pinMode(STAT_LED, OUTPUT);
}

void loop()
{
    // Flash LED
    digitalWrite(STAT_LED, HIGH);
    delay(1000);
    digitalWrite(STAT_LED, LOW);
    delay(1000);
}
