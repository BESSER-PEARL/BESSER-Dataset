





import java.util.List;
import java.util.ArrayList;

public class kmlogo_asm_LogoProgram  {






    private List<Instruction> instructions;


    public kmlogo_asm_LogoProgram(
    ) {
        this.instructions = new ArrayList<>();
    }

    public kmlogo_asm_LogoProgram(
        ArrayList<Instruction> instructions    ) {
        this.instructions = instructions;
    }


    public List<Instruction> getInstructions() {
        return instructions;
    }

    public void addInstruction(Instruction instruction) {
        this.instructions.add(instruction);
    }

}