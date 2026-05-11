





import java.util.List;
import java.util.ArrayList;

public class logoASM_ProcDeclaration extends Instruction {

    private String name;





    private List<logoASM_Instruction> logoasm_instructions;


    public logoASM_ProcDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
        this.logoasm_instructions = new ArrayList<>();
    }

    public logoASM_ProcDeclaration(
        String name        ArrayList<logoASM_Instruction> logoasm_instructions    ) {
        this.name = name;
        this.logoasm_instructions = logoasm_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<logoASM_Instruction> getLogoasm_instructions() {
        return logoasm_instructions;
    }

    public void addLogoasm_instruction(Logoasm_instruction logoasm_instruction) {
        this.logoasm_instructions.add(logoasm_instruction);
    }

}