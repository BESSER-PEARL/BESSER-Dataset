





import java.util.List;
import java.util.ArrayList;

public class fsm_Language  {

    private String name;
    private String target;





    private fsm_Model fsm_model;


    public fsm_Language(
        String name,        String target    ) {
        this.name = name;
        this.target = target;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    public fsm_Model getFsm_model() {
        return fsm_model;
    }

    public void setFsm_model(fsm_Model fsm_model) {
        this.fsm_model = fsm_model;
    }

}