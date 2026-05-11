





import java.util.List;
import java.util.ArrayList;

public class cbpmn_Branch  {

    private boolean default;





    private cbpmn_ProcessModel cbpmn_processmodel;


    public cbpmn_Branch(
        boolean default    ) {
        this.default = default;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }

    public cbpmn_ProcessModel getCbpmn_processmodel() {
        return cbpmn_processmodel;
    }

    public void setCbpmn_processmodel(cbpmn_ProcessModel cbpmn_processmodel) {
        this.cbpmn_processmodel = cbpmn_processmodel;
    }

}