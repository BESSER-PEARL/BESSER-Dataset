





import java.util.List;
import java.util.ArrayList;

public class HALL_FSM_NamedState extends State {

    private String name;





    private FSM fsm;


    public HALL_FSM_NamedState(
        String name    ) {
        super(
        );
        this.name = name;
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