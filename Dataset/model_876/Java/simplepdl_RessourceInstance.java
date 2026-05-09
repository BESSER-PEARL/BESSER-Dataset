





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceInstance extends ProcessElement {

    private int instances;





    private simplepdl_RessourceDefinition simplepdl_ressourcedefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;


    public simplepdl_RessourceInstance(
        int instances    ) {
        super(
        );
        this.instances = instances;
    }


    public int getInstances() {
        return instances;
    }

    public void setInstances(int instances) {
        this.instances = instances;
    }

    public simplepdl_RessourceDefinition getSimplepdl_ressourcedefinition() {
        return simplepdl_ressourcedefinition;
    }

    public void setSimplepdl_ressourcedefinition(simplepdl_RessourceDefinition simplepdl_ressourcedefinition) {
        this.simplepdl_ressourcedefinition = simplepdl_ressourcedefinition;
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