





import java.util.List;
import java.util.ArrayList;

public class nabla_InstructionBlock extends Instruction {






    private List<nabla_Instruction> nabla_instructions;


    public nabla_InstructionBlock(
    ) {
        super(
        );
        this.nabla_instructions = new ArrayList<>();
    }

    public nabla_InstructionBlock(
        ArrayList<nabla_Instruction> nabla_instructions    ) {
        this.nabla_instructions = nabla_instructions;
    }


    public List<nabla_Instruction> getNabla_instructions() {
        return nabla_instructions;
    }

    public void addNabla_instruction(Nabla_instruction nabla_instruction) {
        this.nabla_instructions.add(nabla_instruction);
    }

}