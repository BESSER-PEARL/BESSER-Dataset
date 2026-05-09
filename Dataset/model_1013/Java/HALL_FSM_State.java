





import java.util.List;
import java.util.ArrayList;

public class HALL_FSM_State  {

    private boolean isActive;
    private String name;





    private FSM fsm;


    public HALL_FSM_State(
        boolean isActive,        String name    ) {
        this.isActive = isActive;
        this.name = name;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FSM getFsm() {
        return fsm;
    }

    public void setFsm(FSM fsm) {
        this.fsm = fsm;
    }

}