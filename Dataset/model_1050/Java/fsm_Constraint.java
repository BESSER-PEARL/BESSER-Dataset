





import java.util.List;
import java.util.ArrayList;

public class fsm_Constraint  {

    private String name;
    private boolean true;





    private fsm_Model fsm_model;


    public fsm_Constraint(
        String name,        boolean true    ) {
        this.name = name;
        this.true = true;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getTrue() {
        return true;
    }

    public void setTrue(boolean true) {
        this.true = true;
    }

    public fsm_Model getFsm_model() {
        return fsm_model;
    }

    public void setFsm_model(fsm_Model fsm_model) {
        this.fsm_model = fsm_model;
    }

}