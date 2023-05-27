library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use STD.ENV.ALL;

entity UART_tb is
--  Port ( );
end UART_tb;

architecture Behavioral of UART_tb is

	-- Unit Under Test (UUT)
	Component UART is
		port (
			CLK        : in STD_LOGIC;
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
	end Component;

	-- Internal Inputs to UUT
	signal CLK        :  STD_LOGIC := '0';
	signal RESET   :  STD_LOGIC := '0';
	signal RxD        :  STD_LOGIC := '0';
	signal Rx_Read    :  STD_LOGIC := '0';
	signal Tx_Write   :  STD_LOGIC := '0';
	signal Tx_Data    :  STD_LOGIC := '0';

	-- External Outputs to UUT
	signal Rx_Data    :  STD_LOGIC_VECTOR(7 downto 0);
	signal Rx_Valid   :  STD_LOGIC;
	signal Rx_PError  :  STD_LOGIC;
	signal Tx_D       :  STD_LOGIC;
	signal Tx_Ready   :  STD_LOGIC;

	-- Clock period definitions
	constant CLK_period : time := 10 ns;

begin

	-- Instantiate the Unit Under Test (UUT)
	uut: UART
		port map(
			CLK => CLK,
			RESET => RESET,
			RxD => RxD,
			Rx_Read => Rx_Read,
			Tx_Write => Tx_Write,
			Tx_Data => Tx_Data,
			Rx_Data => Rx_Data,
			Rx_Valid => Rx_Valid,
			Rx_PError => Rx_PError,
			Tx_D => Tx_D,
			Tx_Ready => Tx_Ready
				);

	-- H diadiakasia gia na dhmiourgisoume to roloi
	CLK_process : process
	begin
		CLK <= '0';
		wait for clk_period/2;
		CLK <= '1';
		wait for clk_period/2;
	end process;

	-- Stimulus process definition
	Stimulus_process: process

	begin

		--  Syncronous RESET is deasserted on CLK falling edge
		--  after GSR signal disable (it remains enabled for 100 ns)

		wait for 100 ns;
		wait until (CLK = '0' and CLK'event);

		-- UUT inputs are asserted and deasserted on CLK falling edge

		wait for clk_period;

		-- Message and stimulation end
		report "TEST COMPLETED";
		stop(2);

	end process;


end Behavioral;