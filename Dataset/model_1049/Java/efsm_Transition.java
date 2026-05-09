





import java.util.List;
import java.util.ArrayList;

public class efsm_Transition  {

    private String name;
    private String guard;
    private String output;
    private String action;





    private efsm_EFSM efsm_efsm;


    public efsm_Transition(
        String name,        String guard,        String output,        String action    ) {
        this.name = name;
        this.guard = guard;
        this.output = output;
        this.action = action;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public efsm_EFSM getEfsm_efsm() {
        return efsm_efsm;
    }

    public void setEfsm_efsm(efsm_EFSM efsm_efsm) {
        this.efsm_efsm = efsm_efsm;
    }

}