





import java.util.List;
import java.util.ArrayList;

public class ir_Loop extends IterableInstruction {

    private boolean multithreadable;





    private ir_Instruction ir_instruction;


    public ir_Loop(
        boolean multithreadable    ) {
        super(
        );
        this.multithreadable = multithreadable;
    }


    public boolean getMultithreadable() {
        return multithreadable;
    }

    public void setMultithreadable(boolean multithreadable) {
        this.multithreadable = multithreadable;
    }

    public ir_Instruction getIr_instruction() {
        return ir_instruction;
    }

    public void setIr_instruction(ir_Instruction ir_instruction) {
        this.ir_instruction = ir_instruction;
    }

}