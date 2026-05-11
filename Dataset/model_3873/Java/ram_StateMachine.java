





import java.util.List;
import java.util.ArrayList;

public class ram_StateMachine  {






    private ram_StateView ram_stateview;




    private ram_CheckState ram_checkstate;




    private List<ram_Transition> ram_transitions;




    private List<ram_CheckState> ram_checkstates;


    public ram_StateMachine(
    ) {
        this.ram_transitions = new ArrayList<>();
        this.ram_checkstates = new ArrayList<>();
    }

    public ram_StateMachine(
        ArrayList<ram_Transition> ram_transitions,        ArrayList<ram_CheckState> ram_checkstates    ) {
        this.ram_transitions = ram_transitions;
        this.ram_checkstates = ram_checkstates;
    }


    public ram_StateView getRam_stateview() {
        return ram_stateview;
    }

    public void setRam_stateview(ram_StateView ram_stateview) {
        this.ram_stateview = ram_stateview;
    }
    public ram_CheckState getRam_checkstate() {
        return ram_checkstate;
    }

    public void setRam_checkstate(ram_CheckState ram_checkstate) {
        this.ram_checkstate = ram_checkstate;
    }
    public List<ram_Transition> getRam_transitions() {
        return ram_transitions;
    }

    public void addRam_transition(Ram_transition ram_transition) {
        this.ram_transitions.add(ram_transition);
    }
    public List<ram_CheckState> getRam_checkstates() {
        return ram_checkstates;
    }

    public void addRam_checkstate(Ram_checkstate ram_checkstate) {
        this.ram_checkstates.add(ram_checkstate);
    }

}