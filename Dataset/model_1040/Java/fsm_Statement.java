





import java.util.List;
import java.util.ArrayList;

public class fsm_Statement  {






    private fsm_Transition fsm_transition;




    private fsm_Block fsm_block;


    public fsm_Statement(
    ) {
    }



    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }
    public fsm_Block getFsm_block() {
        return fsm_block;
    }

    public void setFsm_block(fsm_Block fsm_block) {
        this.fsm_block = fsm_block;
    }

}