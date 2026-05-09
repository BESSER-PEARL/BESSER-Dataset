





import java.util.List;
import java.util.ArrayList;

public class statemachine_Constant  {

    private String name;





    private statemachine_ConstantRef statemachine_constantref;




    private statemachine_Statemachine statemachine_statemachine;


    public statemachine_Constant(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_ConstantRef getStatemachine_constantref() {
        return statemachine_constantref;
    }

    public void setStatemachine_constantref(statemachine_ConstantRef statemachine_constantref) {
        this.statemachine_constantref = statemachine_constantref;
    }
    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}