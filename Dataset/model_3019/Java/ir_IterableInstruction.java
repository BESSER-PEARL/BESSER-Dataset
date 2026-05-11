





import java.util.List;
import java.util.ArrayList;

public class ir_IterableInstruction extends Instruction {






    private ir_IterationBlock ir_iterationblock;


    public ir_IterableInstruction(
    ) {
        super(
        );
    }



    public ir_IterationBlock getIr_iterationblock() {
        return ir_iterationblock;
    }

    public void setIr_iterationblock(ir_IterationBlock ir_iterationblock) {
        this.ir_iterationblock = ir_iterationblock;
    }

}