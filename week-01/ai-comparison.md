I tested the same factual question with two different AI assistants.
Question asked to both tools:  
What is the difference between RAM and ROM?

 ChatGPT :
| RAM                                    | ROM                                                                     |
| Random Access Memory                   | Read-Only Memory                                                        |
| Temporary memory                       | Non-volatile memory                                                     |
| Data is lost when power is turned off  | Data is retained when power is turned off |
| Used while the computer is running     | Used to store firmware/startup instructions |
| Can be read and written frequently     | Traditionally mainly read; modern ROM types can be rewritten in certain ways |
| Example: programs currently running    | Example: firmware used during device startup |

RAM = Working memory → temporary
ROM = Stored instructions → remains after power is off.
 
 Gemini :
 RAM and ROM serve two entirely different roles in a computer or microcontroller system. 
RAM (Random Access Memory): acts as the system's temporary workspace. It is volatile memory, meaning all data stored in RAM disappears as soon as power is disconnected. Whenever you run applications, open software, or process live sensor data, the processor dynamically reads from and writes to RAM because of its extremely high speed and low latency.

ROM (Read-Only Memory) :on the other hand, is non-volatile memory designed for permanent or long-term storage. It retains its contents even when the device is completely powered down. ROM comes pre-programmed with critical system instructions—on a PC or the bootloader on a microcontroller—that tell the hardware how to initialize and start up properly before any operating system or application code is executed into RAM.

--> Evidence
I checked the important claims from both answers against a reliable technical source.
Verification source:  
[IBM - What is Primary Storage?] (https://www.ibm.com/think/topics/primary-storage)
Verified claim:
The claim that RAM is temporary memory while ROM retains its data when the power is turned off was supported by the IBM reference.

--> Verification
I compared the answers from both AI assistants with the reference source instead of assuming that a confident-sounding answer was automatically correct. The main points about RAM and ROM were correct based on the reference.

--> Reflection
This experiment showed me that two AI assistants can give similar answers, but that does not automatically make the information correct. Checking important claims against a reliable source gives more confidence in the result. It also showed me why AI output should be treated as information to verify rather than final proof.
