





import java.util.List;
import java.util.ArrayList;

public class fsm_Statement  {






    private fsm_Transition fsm_transition;




    private fsm_Program fsm_program;


    public fsm_Statement(
    ) {
    }



    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_Program getFsm_program() {
        return fsm_program;
    }

    public void setFsm_program(fsm_Program fsm_program) {
        this.fsm_program = fsm_program;
    }

}