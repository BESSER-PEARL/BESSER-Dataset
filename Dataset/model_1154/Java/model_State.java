





import java.util.List;
import java.util.ArrayList;

public class model_State  {

    private String name;





    private model_FSM model_fsm;


    public model_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_FSM getModel_fsm() {
        return model_fsm;
    }

    public void setModel_fsm(model_FSM model_fsm) {
        this.model_fsm = model_fsm;
    }

}