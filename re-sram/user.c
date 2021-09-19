/*
	atmega328p_dummy_blinky.c

	Copyright 2008, 2009 Michel Pollet <buserror@gmail.com>

 	This file is part of simavr.

	simavr is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	simavr is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with simavr.  If not, see <http://www.gnu.org/licenses/>.
 */


#ifdef F_CPU
#undef F_CPU
#endif

#define F_CPU 16000000

#include <avr/io.h>
#include <stdio.h>
#include <avr/interrupt.h>
#include <avr/eeprom.h>
#include <avr/sleep.h>

/*
 * This demonstrate how to use the avr_mcu_section.h file
 * The macro adds a section to the ELF file with useful
 * information for the simulator
 */
#include "avr_mcu_section.h"

#define SRAM_START 0x0100
#define SRAM_INTERNAL_END 0x21FF
#define SRAM_EXTERNAL_END 0xFFFF

AVR_MCU(F_CPU, "atmega2560");

static int uart_putchar(char c, FILE *stream) {
  //if (c == '\n')
  //  uart_putchar('\r', stream);
  loop_until_bit_is_set(UCSR0A, UDRE0);
  UDR0 = c;
  return 0;
}

static FILE mystdout = FDEV_SETUP_STREAM(uart_putchar, NULL,
                                         _FDEV_SETUP_WRITE);


int main()
{
	stdout = &mystdout;

	printf("Bootloader properly programmed, and ran me! Huzzah!\n");

	for (uint8_t* i=SRAM_START;i <= SRAM_INTERNAL_END; i=i+8) {
		printf("%02X %02X %02X %02X %02X %02X %02X %02X\r\n", i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]);
	};
	
	while (1) {
		// read from 0x0100-0x08FF

		
	};
}

