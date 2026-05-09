





import java.util.List;
import java.util.ArrayList;

public class spem_WorkProductDefinitionRelationship extends MethodContentElement {






    private List<spem_WorkProductDefinition> spem_workproductdefinitions;




    private spem_WorkProductDefinition spem_workproductdefinition;


    public spem_WorkProductDefinitionRelationship(
    ) {
        super(
        );
        this.spem_workproductdefinitions = new ArrayList<>();
    }

    public spem_WorkProductDefinitionRelationship(
        ArrayList<spem_WorkProductDefinition> spem_workproductdefinitions    ) {
        this.spem_workproductdefinitions = spem_workproductdefinitions;
    }


    public List<spem_WorkProductDefinition> getSpem_workproductdefinitions() {
        return spem_workproductdefinitions;
    }

    public void addSpem_workproductdefinition(Spem_workproductdefinition spem_workproductdefinition) {
        this.spem_workproductdefinitions.add(spem_workproductdefinition);
    }
    public spem_WorkProductDefinition getSpem_workproductdefinition() {
        return spem_workproductdefinition;
    }

    public void setSpem_workproductdefinition(spem_WorkProductDefinition spem_workproductdefinition) {
        this.spem_workproductdefinition = spem_workproductdefinition;
    }

}