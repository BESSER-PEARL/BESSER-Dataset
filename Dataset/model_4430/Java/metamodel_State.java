





import java.util.List;
import java.util.ArrayList;

public class metamodel_State  {

    private boolean isInitial;
    private String name;
    private int uid;





    private metamodel_StateMachine metamodel_statemachine;




    private metamodel_Action metamodel_action;




    private metamodel_Action metamodel_action;




    private metamodel_Action metamodel_action;


    public metamodel_State(
        boolean isInitial,        String name,        int uid    ) {
        this.isInitial = isInitial;
        this.name = name;
        this.uid = uid;
    }


    public boolean getIsinitial() {
        return isInitial;
    }

    public void setIsinitial(boolean isInitial) {
        this.isInitial = isInitial;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getUid() {
        return uid;
    }

    public void setUid(int uid) {
        this.uid = uid;
    }

    public metamodel_StateMachine getMetamodel_statemachine() {
        return metamodel_statemachine;
    }

    public void setMetamodel_statemachine(metamodel_StateMachine metamodel_statemachine) {
        this.metamodel_statemachine = metamodel_statemachine;
    }
    public metamodel_Action getMetamodel_action() {
        return metamodel_action;
    }

    public void setMetamodel_action(metamodel_Action metamodel_action) {
        this.metamodel_action = metamodel_action;
    }
    public metamodel_Action getMetamodel_action() {
        return metamodel_action;
    }

    public void setMetamodel_action(metamodel_Action metamodel_action) {
        this.metamodel_action = metamodel_action;
    }
    public metamodel_Action getMetamodel_action() {
        return metamodel_action;
    }

    public void setMetamodel_action(metamodel_Action metamodel_action) {
        this.metamodel_action = metamodel_action;
    }

}