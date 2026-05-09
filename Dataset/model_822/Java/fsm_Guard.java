





import java.util.List;
import java.util.ArrayList;

public class fsm_Guard  {

    private boolean not_;





    private fsm_Transition fsm_transition;


    public fsm_Guard(
        boolean not_    ) {
        this.not_ = not_;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }

    public fsm_Transition getFsm_transition() {
        return fsm_transition;
    }

    public void setFsm_transition(fsm_Transition fsm_transition) {
        this.fsm_transition = fsm_transition;
    }

}