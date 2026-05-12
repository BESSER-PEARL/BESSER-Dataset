





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_State extends AbstractState {

    private String name;





    private scxmlxt_StateMachine scxmlxt_statemachine;


    public scxmlxt_State(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public scxmlxt_StateMachine getScxmlxt_statemachine() {
        return scxmlxt_statemachine;
    }

    public void setScxmlxt_statemachine(scxmlxt_StateMachine scxmlxt_statemachine) {
        this.scxmlxt_statemachine = scxmlxt_statemachine;
    }

}