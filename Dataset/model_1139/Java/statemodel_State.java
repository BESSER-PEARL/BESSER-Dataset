





import java.util.List;
import java.util.ArrayList;

public class statemodel_State extends Element, Activity {

    private String name;
    private String type;





    private statemodel_Statemachine statemodel_statemachine;


    public statemodel_State(
        String name,        String type    ) {
        super(
        );
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public statemodel_Statemachine getStatemodel_statemachine() {
        return statemodel_statemachine;
    }

    public void setStatemodel_statemachine(statemodel_Statemachine statemodel_statemachine) {
        this.statemodel_statemachine = statemodel_statemachine;
    }

}