





import java.util.List;
import java.util.ArrayList;

public class ir_InstructionBlock extends Instruction {






    private List<ir_Instruction> ir_instructions;




    private List<ir_Variable> ir_variables;


    public ir_InstructionBlock(
    ) {
        super(
        );
        this.ir_instructions = new ArrayList<>();
        this.ir_variables = new ArrayList<>();
    }

    public ir_InstructionBlock(
        ArrayList<ir_Instruction> ir_instructions,        ArrayList<ir_Variable> ir_variables    ) {
        this.ir_instructions = ir_instructions;
        this.ir_variables = ir_variables;
    }


    public List<ir_Instruction> getIr_instructions() {
        return ir_instructions;
    }

    public void addIr_instruction(Ir_instruction ir_instruction) {
        this.ir_instructions.add(ir_instruction);
    }
    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }

}