





import java.util.List;
import java.util.ArrayList;

public class dsl_Event  {

    private String name;





    private dsl_StateMachine dsl_statemachine;


    public dsl_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_StateMachine getDsl_statemachine() {
        return dsl_statemachine;
    }

    public void setDsl_statemachine(dsl_StateMachine dsl_statemachine) {
        this.dsl_statemachine = dsl_statemachine;
    }

}