





import java.util.List;
import java.util.ArrayList;

public class fsm_StateMachine  {

    private String name;





    private fsm_Root fsm_root;


    public fsm_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsm_Root getFsm_root() {
        return fsm_root;
    }

    public void setFsm_root(fsm_Root fsm_root) {
        this.fsm_root = fsm_root;
    }

}