/*
   Copyright (c) 2023 Boot&Work Corp., S.L. All rights reserved

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <Arduino.h>


// Include Industrial Shields libraries
#include <DALI.h>

//// IMPORTANT: check switches configuration


DALI dali(18, 19);

uint8_t value = 0;
uint32_t lastStepTime = millis();

////////////////////////////////////////////////////////////////////////////////////////////////////
void setup() {
  Serial.begin(9600UL);

  dali.begin();
}

////////////////////////////////////////////////////////////////////////////////////////////////////
void loop() {
  if (millis() - lastStepTime > 5) {
    value += 10;
    if (value > 254) {
      value = 0;
    }

    dali.setValue(6, value);

    lastStepTime = millis();
  }
}
