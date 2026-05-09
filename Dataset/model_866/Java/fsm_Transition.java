





import java.util.List;
import java.util.ArrayList;

public class fsm_Transition  {

    private String Guard;
    private String Effect;





    private fsm_State fsm_state;


    public fsm_Transition(
        String Guard,        String Effect    ) {
        this.Guard = Guard;
        this.Effect = Effect;
    }


    public String getGuard() {
        return Guard;
    }

    public void setGuard(String Guard) {
        this.Guard = Guard;
    }
    public String getEffect() {
        return Effect;
    }

    public void setEffect(String Effect) {
        this.Effect = Effect;
    }

    public fsm_State getFsm_state() {
        return fsm_state;
    }

    public void setFsm_state(fsm_State fsm_state) {
        this.fsm_state = fsm_state;
    }

}