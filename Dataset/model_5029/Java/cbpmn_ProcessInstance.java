





import java.util.List;
import java.util.ArrayList;

public class cbpmn_ProcessInstance  {

    private String id;





    private cbpmn_ProcessModel cbpmn_processmodel;


    public cbpmn_ProcessInstance(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public cbpmn_ProcessModel getCbpmn_processmodel() {
        return cbpmn_processmodel;
    }

    public void setCbpmn_processmodel(cbpmn_ProcessModel cbpmn_processmodel) {
        this.cbpmn_processmodel = cbpmn_processmodel;
    }

}