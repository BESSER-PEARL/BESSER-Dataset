





import java.util.List;
import java.util.ArrayList;

public class StateMachineDiagram_Meta_StateMachine  {

    private String name;





    private StateMachineDiagram_Meta_State statemachinediagram_meta_state;




    private StateMachineDiagram_Meta_Application statemachinediagram_meta_application;


    public StateMachineDiagram_Meta_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public StateMachineDiagram_Meta_State getStatemachinediagram_meta_state() {
        return statemachinediagram_meta_state;
    }

    public void setStatemachinediagram_meta_state(StateMachineDiagram_Meta_State statemachinediagram_meta_state) {
        this.statemachinediagram_meta_state = statemachinediagram_meta_state;
    }
    public StateMachineDiagram_Meta_Application getStatemachinediagram_meta_application() {
        return statemachinediagram_meta_application;
    }

    public void setStatemachinediagram_meta_application(StateMachineDiagram_Meta_Application statemachinediagram_meta_application) {
        this.statemachinediagram_meta_application = statemachinediagram_meta_application;
    }

}