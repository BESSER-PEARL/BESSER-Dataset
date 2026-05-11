





import java.util.List;
import java.util.ArrayList;

public class logoASM_LogoProgram  {






    private List<logoASM_Instruction> logoasm_instructions;


    public logoASM_LogoProgram(
    ) {
        this.logoasm_instructions = new ArrayList<>();
    }

    public logoASM_LogoProgram(
        ArrayList<logoASM_Instruction> logoasm_instructions    ) {
        this.logoasm_instructions = logoasm_instructions;
    }


    public List<logoASM_Instruction> getLogoasm_instructions() {
        return logoasm_instructions;
    }

    public void addLogoasm_instruction(Logoasm_instruction logoasm_instruction) {
        this.logoasm_instructions.add(logoasm_instruction);
    }

}