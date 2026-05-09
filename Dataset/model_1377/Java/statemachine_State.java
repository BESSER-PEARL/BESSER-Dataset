





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String id;
    private boolean initial;
    private String name;
    private boolean final;





    private statemachine_Statemachine statemachine_statemachine;




    private statemachine_StatePropertyExpression statemachine_statepropertyexpression;


    public statemachine_State(
        String id,        boolean initial,        String name,        boolean final    ) {
        this.id = id;
        this.initial = initial;
        this.name = name;
        this.final = final;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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

    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }
    public statemachine_StatePropertyExpression getStatemachine_statepropertyexpression() {
        return statemachine_statepropertyexpression;
    }

    public void setStatemachine_statepropertyexpression(statemachine_StatePropertyExpression statemachine_statepropertyexpression) {
        this.statemachine_statepropertyexpression = statemachine_statepropertyexpression;
    }

}