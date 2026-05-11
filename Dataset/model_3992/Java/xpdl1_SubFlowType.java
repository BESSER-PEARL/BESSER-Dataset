





import java.util.List;
import java.util.ArrayList;

public class xpdl1_SubFlowType  {

    private String execution;
    private String id;





    private xpdl1_ImplementationType xpdl1_implementationtype;




    private xpdl1_ActualParametersType xpdl1_actualparameterstype;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_SubFlowType(
        String execution,        String id    ) {
        this.execution = execution;
        this.id = id;
    }


    public String getExecution() {
        return execution;
    }

    public void setExecution(String execution) {
        this.execution = execution;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xpdl1_ImplementationType getXpdl1_implementationtype() {
        return xpdl1_implementationtype;
    }

    public void setXpdl1_implementationtype(xpdl1_ImplementationType xpdl1_implementationtype) {
        this.xpdl1_implementationtype = xpdl1_implementationtype;
    }
    public xpdl1_ActualParametersType getXpdl1_actualparameterstype() {
        return xpdl1_actualparameterstype;
    }

    public void setXpdl1_actualparameterstype(xpdl1_ActualParametersType xpdl1_actualparameterstype) {
        this.xpdl1_actualparameterstype = xpdl1_actualparameterstype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}