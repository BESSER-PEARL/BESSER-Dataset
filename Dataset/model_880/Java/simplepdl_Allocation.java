





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Allocation  {

    private int needed;





    private simplepdl_Ressource simplepdl_ressource;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;


    public simplepdl_Allocation(
        int needed    ) {
        this.needed = needed;
    }


    public int getNeeded() {
        return needed;
    }

    public void setNeeded(int needed) {
        this.needed = needed;
    }

    public simplepdl_Ressource getSimplepdl_ressource() {
        return simplepdl_ressource;
    }

    public void setSimplepdl_ressource(simplepdl_Ressource simplepdl_ressource) {
        this.simplepdl_ressource = simplepdl_ressource;
    }
    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }
    public simplepdl_WorkDefinition getSimplepdl_workdefinition() {
        return simplepdl_workdefinition;
    }

    public void setSimplepdl_workdefinition(simplepdl_WorkDefinition simplepdl_workdefinition) {
        this.simplepdl_workdefinition = simplepdl_workdefinition;
    }

}