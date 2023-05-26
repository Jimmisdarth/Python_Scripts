library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
--use IEEE.NUMERIC_STD.ALL;


entity UART is
	Port ( 
		CLK		   : in STD_LOGIC;
		RESET	   : in STD_LOGIC;
		
		RxD        : in STD_LOGIC;
		
		Rx_Read    : in STD_LOGIC;
		
		Tx_Write   : in STD_LOGIC;
		Tx_Data    : in STD_LOGIC;
		
		Rx_Data    : out STD_LOGIC_VECTOR(7 downto 0);
		Rx_Valid   : out STD_LOGIC;
		Rx_PError  : out STD_LOGIC;
		
		Tx_D       : out STD_LOGIC;
		
		Tx_Ready   : out STD_LOGIC);
end UART;

architecture Behavioral of UART is

begin


end Behavioral;