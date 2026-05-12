





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private boolean initial;
    private boolean final;
    private String id;
    private String name;





    private statemachine_Statemachine statemachine_statemachine;


    public statemachine_State(
        boolean initial,        boolean final,        String id,        String name    ) {
        this.initial = initial;
        this.final = final;
        this.id = id;
        this.name = name;
    }


    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}