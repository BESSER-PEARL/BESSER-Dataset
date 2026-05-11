





import java.util.List;
import java.util.ArrayList;

public class xpdl1_WorkflowProcessesType  {






    private xpdl1_PackageType xpdl1_packagetype;




    private List<xpdl1_WorkflowProcessType> xpdl1_workflowprocesstypes;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_WorkflowProcessesType(
    ) {
        this.xpdl1_workflowprocesstypes = new ArrayList<>();
    }

    public xpdl1_WorkflowProcessesType(
        ArrayList<xpdl1_WorkflowProcessType> xpdl1_workflowprocesstypes    ) {
        this.xpdl1_workflowprocesstypes = xpdl1_workflowprocesstypes;
    }


    public xpdl1_PackageType getXpdl1_packagetype() {
        return xpdl1_packagetype;
    }

    public void setXpdl1_packagetype(xpdl1_PackageType xpdl1_packagetype) {
        this.xpdl1_packagetype = xpdl1_packagetype;
    }
    public List<xpdl1_WorkflowProcessType> getXpdl1_workflowprocesstypes() {
        return xpdl1_workflowprocesstypes;
    }

    public void addXpdl1_workflowprocesstype(Xpdl1_workflowprocesstype xpdl1_workflowprocesstype) {
        this.xpdl1_workflowprocesstypes.add(xpdl1_workflowprocesstype);
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}