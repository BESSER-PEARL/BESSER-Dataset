





import java.util.List;
import java.util.ArrayList;

public class fsm_State  {

    private boolean initial;
    private String name;
    private boolean final;





    private fsm_Machine fsm_machine;


    public fsm_State(
        boolean initial,        String name,        boolean final    ) {
        this.initial = initial;
        this.name = name;
        this.final = final;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public fsm_Machine getFsm_machine() {
        return fsm_machine;
    }

    public void setFsm_machine(fsm_Machine fsm_machine) {
        this.fsm_machine = fsm_machine;
    }

}