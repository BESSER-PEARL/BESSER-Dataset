





import java.util.List;
import java.util.ArrayList;

public class efsm_Transition  {

    private String name;
    private String action;
    private String output;
    private String input;
    private String guard;
    private String event;





    private efsm_EFSM efsm_efsm;


    public efsm_Transition(
        String name,        String action,        String output,        String input,        String guard,        String event    ) {
        this.name = name;
        this.action = action;
        this.output = output;
        this.input = input;
        this.guard = guard;
        this.event = event;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public efsm_EFSM getEfsm_efsm() {
        return efsm_efsm;
    }

    public void setEfsm_efsm(efsm_EFSM efsm_efsm) {
        this.efsm_efsm = efsm_efsm;
    }

}