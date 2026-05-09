





import java.util.List;
import java.util.ArrayList;

public class oclstates_Statemachine  {

    private boolean initial;
    private String name;
    private int value;





    private oclstates_Module oclstates_module;


    public oclstates_Statemachine(
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

    public oclstates_Module getOclstates_module() {
        return oclstates_module;
    }

    public void setOclstates_module(oclstates_Module oclstates_module) {
        this.oclstates_module = oclstates_module;
    }

}