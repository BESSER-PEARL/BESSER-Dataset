





import java.util.List;
import java.util.ArrayList;

public class simplepdl_Parameter extends ProcessElement {

    private int nbNeeds;
    private String name;





    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_WorkDefinition simplepdl_workdefinition;




    private simplepdl_Resource simplepdl_resource;


    public simplepdl_Parameter(
        int nbNeeds,        String name    ) {
        super(
        );
        this.nbNeeds = nbNeeds;
        this.name = name;
    }


    public int getNbneeds() {
        return nbNeeds;
    }

    public void setNbneeds(int nbNeeds) {
        this.nbNeeds = nbNeeds;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public simplepdl_Resource getSimplepdl_resource() {
        return simplepdl_resource;
    }

    public void setSimplepdl_resource(simplepdl_Resource simplepdl_resource) {
        this.simplepdl_resource = simplepdl_resource;
    }

}