





import java.util.List;
import java.util.ArrayList;

public class ir_ReductionInstruction extends IterableInstruction {






    private ir_SimpleVariable ir_simplevariable;




    private List<ir_Instruction> ir_instructions;




    private ir_Expression ir_expression;




    private ir_Function ir_function;


    public ir_ReductionInstruction(
    ) {
        super(
        );
        this.ir_instructions = new ArrayList<>();
    }

    public ir_ReductionInstruction(
        ArrayList<ir_Instruction> ir_instructions    ) {
        this.ir_instructions = ir_instructions;
    }


    public ir_SimpleVariable getIr_simplevariable() {
        return ir_simplevariable;
    }

    public void setIr_simplevariable(ir_SimpleVariable ir_simplevariable) {
        this.ir_simplevariable = ir_simplevariable;
    }
    public List<ir_Instruction> getIr_instructions() {
        return ir_instructions;
    }

    public void addIr_instruction(Ir_instruction ir_instruction) {
        this.ir_instructions.add(ir_instruction);
    }
    public ir_Expression getIr_expression() {
        return ir_expression;
    }

    public void setIr_expression(ir_Expression ir_expression) {
        this.ir_expression = ir_expression;
    }
    public ir_Function getIr_function() {
        return ir_function;
    }

    public void setIr_function(ir_Function ir_function) {
        this.ir_function = ir_function;
    }

}