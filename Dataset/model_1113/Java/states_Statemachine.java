





import java.util.List;
import java.util.ArrayList;

public class states_Statemachine  {

    private int value;
    private boolean initial;
    private String name;





    private states_Module states_module;


    public states_Statemachine(
        int value,        boolean initial,        String name    ) {
        this.value = value;
        this.initial = initial;
        this.name = name;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
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

    public states_Module getStates_module() {
        return states_module;
    }

    public void setStates_module(states_Module states_module) {
        this.states_module = states_module;
    }

}