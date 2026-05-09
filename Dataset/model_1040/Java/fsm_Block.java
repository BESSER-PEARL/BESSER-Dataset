





import java.util.List;
import java.util.ArrayList;

public class fsm_Block extends Statement {






    private fsm_Conditional fsm_conditional;




    private fsm_Loop fsm_loop;


    public fsm_Block(
    ) {
        super(
        );
    }



    public fsm_Conditional getFsm_conditional() {
        return fsm_conditional;
    }

    public void setFsm_conditional(fsm_Conditional fsm_conditional) {
        this.fsm_conditional = fsm_conditional;
    }
    public fsm_Loop getFsm_loop() {
        return fsm_loop;
    }

    public void setFsm_loop(fsm_Loop fsm_loop) {
        this.fsm_loop = fsm_loop;
    }

}