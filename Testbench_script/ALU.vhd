library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU is
	Port ( 
		a 		:  in STD_LOGIC_VECTOR (2 downto 0);
		b 		:  in STD_LOGIC_VECTOR (2 downto 0);
		
		Control :  in STD_LOGIC;	
		
		Result  : out STD_LOGIC_VECTOR (2 downto 0);
		OVF 	: out STD_LOGIC;
		Carry   : out STD_LOGIC);
end ALU;

-- entity ALU is
	-- Generic (WIDTH : positive := 3);
	-- Port ( 
		-- a 	   :  in STD_LOGIC_VECTOR (WIDTH-1 downto 0);
		-- b 	   :  in STD_LOGIC_VECTOR (WIDTH-1 downto 0);
		
		-- Control :  in STD_LOGIC;	
		
		-- Result  : out STD_LOGIC_VECTOR (WIDTH-1 downto 0);
		-- OVF 	   : out STD_LOGIC;
		-- Carry   : out STD_LOGIC);
-- end ALU;

architecture DataFlow_A of ALU is

signal Control_Vector : STD_LOGIC_VECTOR (2 downto 0);

signal a_S   : SIGNED (4 downto 0);
signal b_S   : SIGNED (4 downto 0);

signal Sum      : STD_LOGIC_VECTOR (4 downto 0);
signal OVF_in   : STD_LOGIC;
signal Carry_in : STD_LOGIC;

signal Division : STD_LOGIC_VECTOR (2 downto 0);

begin

	Control_Vector <= (others => Control);

	a_S <= signed('0'&a(2)&a);
	b_S <= signed('0'&b(2)&b);
	
	Sum  <= std_logic_vector(a_s - b_s);
	OVF_in  <= Sum(3) xor Sum(2);
	Carry_in <= Sum(4);
	
	Division <= std_logic_vector(SHIFT_RIGHT (signed(b), 1));
	
	-- ousiastika to mux 2 se 1 wste na dialejoume th swsth ejodo
	Result <= (Sum(2 downto 0) and (not Control_Vector)) or (Division and Control_Vector);
	
	-- H maska wste otan kanoume Diairesh to OVF kai to Carry na einai geiomena
	OVF   <= OVF_in and (not control);
	Carry <= Carry_in and (not control);	

end DataFlow_A;
