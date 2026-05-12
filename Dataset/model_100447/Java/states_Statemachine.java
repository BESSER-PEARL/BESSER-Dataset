





import java.util.List;
import java.util.ArrayList;

public class states_Statemachine  {

    private boolean initial;
    private String name;
    private int value;





    private states_CompoundState states_compoundstate;




    private states_Module states_module;


    public states_Statemachine(
        boolean initial,        String name,        int value    ) {
        this.initial = initial;
        this.name = name;
        this.value = value;
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
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public states_CompoundState getStates_compoundstate() {
        return states_compoundstate;
    }

    public void setStates_compoundstate(states_CompoundState states_compoundstate) {
        this.states_compoundstate = states_compoundstate;
    }
    public states_Module getStates_module() {
        return states_module;
    }

    public void setStates_module(states_Module states_module) {
        this.states_module = states_module;
    }

}