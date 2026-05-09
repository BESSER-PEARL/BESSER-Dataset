





import java.util.List;
import java.util.ArrayList;

public class simplepdl_UseResources extends ProcessElement {

    private int weight;





    private simplepdl_Resource simplepdl_resource;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;


    public simplepdl_UseResources(
        int weight    ) {
        super(
        );
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public simplepdl_Resource getSimplepdl_resource() {
        return simplepdl_resource;
    }

    public void setSimplepdl_resource(simplepdl_Resource simplepdl_resource) {
        this.simplepdl_resource = simplepdl_resource;
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