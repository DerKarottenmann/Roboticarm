// Arduino IDLE
// Arduino UNO
// Download MFRC522 library

// PINS:

// SDA = 10;
// SCK = 13;
// MOSI = 11;
// MISO = 12;
// GND = GND;
// RST = 9;
// 3,3V = 3,3V;

#include "MFRC522.h"

#define SDA 10
#define RST 9

MFRC522 mfrc522(SDA, RST);

void setup()
{
    Serial.begin(9600);
    SPI.begin();

    mfrc522.PCD_Init();
}

void loop()
{
    String WertDEZ;

    if (!mfrc522.PICC_IsNewCardPresent())
    {

        return;
    }

    if (!mfrc522.PICC_ReadCardSerial())
    {

        return;
    }

    Serial.println("Karte entdeckt!");

    for (byte i = 0; i < mfrc522.uid.size; i++)
    {

        WertDEZ = WertDEZ + String(mfrc522.uid.uidByte[i], DEC) + " ";
    }

    Serial.println("Dezimalwert: " + WertDEZ);

    delay(1000);
}

// Jeder Sender hat einen Dezimalwert (in Variable Zahl gespeichert)
//  => Für Erkennung der Figuren Matrix(64 auf 2) anlegen, in denen alle 64 DEZWerte den
//     Zugehörigen Figuren zugewiesen werden(BSP Matrix [[...                ]
//                                                       [4 166 97 64, bauer1]
//                                                       [...                ]] )
