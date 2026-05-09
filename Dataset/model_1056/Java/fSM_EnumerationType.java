





import java.util.List;
import java.util.ArrayList;

public class fSM_EnumerationType  {

    private String name;





    private fSM_Model fsm_model;


    public fSM_EnumerationType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fSM_Model getFsm_model() {
        return fsm_model;
    }

    public void setFsm_model(fSM_Model fsm_model) {
        this.fsm_model = fsm_model;
    }

}