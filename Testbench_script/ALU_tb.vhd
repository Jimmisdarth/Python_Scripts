library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use STD.ENV.ALL;

entity ALU_tb is
--  Port ( );
end ALU_tb;

architecture Behavioral of ALU_tb is

	-- Unit Under Test (UUT)
	Component ALU is
		port (
			a 		:  in STD_LOGIC_VECTOR (2 downto 0);
			b 		:  in STD_LOGIC_VECTOR (2 downto 0);
			Control :  in STD_LOGIC;	
			Result  : out STD_LOGIC_VECTOR (2 downto 0);
			OVF 	: out STD_LOGIC;
			Carry   : out STD_LOGIC);
	end Component;

	-- Internal Inputs to UUT
	signal CLK : STD_LOGIC := '0';
	signal a :   STD_LOGIC_VECTOR (2 downto 0) := (others => '0');
	signal b :   STD_LOGIC_VECTOR (2 downto 0) := (others => '0');
	signal Control :   STD_LOGIC := '0';

	-- External Outputs to UUT
	signal Result  :  STD_LOGIC_VECTOR (2 downto 0);
	signal OVF :  STD_LOGIC;
	signal Carry   :  STD_LOGIC;

	-- Clock period definitions
	constant CLK_period : time := 10 ns;

begin

	-- Instantiate the Unit Under Test (UUT)
	uut: ALU
		port map(
			a => a,
			b => b,
			Control => Control,
			Result => Result,
			OVF => OVF,
			Carry => Carry
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