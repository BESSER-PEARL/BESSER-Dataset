





import java.util.List;
import java.util.ArrayList;

public class model_Catch extends BPELExtensibleElement {

    private String faultName;





    private model_FaultHandler model_faulthandler;




    private model_Activity model_activity;




    private model_Variable model_variable;


    public model_Catch(
        String faultName    ) {
        super(
        );
        this.faultName = faultName;
    }


    public String getFaultname() {
        return faultName;
    }

    public void setFaultname(String faultName) {
        this.faultName = faultName;
    }

    public model_FaultHandler getModel_faulthandler() {
        return model_faulthandler;
    }

    public void setModel_faulthandler(model_FaultHandler model_faulthandler) {
        this.model_faulthandler = model_faulthandler;
    }
    public model_Activity getModel_activity() {
        return model_activity;
    }

    public void setModel_activity(model_Activity model_activity) {
        this.model_activity = model_activity;
    }
    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }

}