





import java.util.List;
import java.util.ArrayList;

public class tp01_State  {

    private String name;





    private tp01_FSM tp01_fsm;


    public tp01_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp01_FSM getTp01_fsm() {
        return tp01_fsm;
    }

    public void setTp01_fsm(tp01_FSM tp01_fsm) {
        this.tp01_fsm = tp01_fsm;
    }

}