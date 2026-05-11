





import java.util.List;
import java.util.ArrayList;

public class kmLogo_ASM_LogoProgram  {






    private List<Instruction> instructions;


    public kmLogo_ASM_LogoProgram(
    ) {
        this.instructions = new ArrayList<>();
    }

    public kmLogo_ASM_LogoProgram(
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