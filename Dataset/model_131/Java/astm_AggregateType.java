





import java.util.List;
import java.util.ArrayList;

public class astm_AggregateType extends DataType {






    private astm_AggregateTypeDefinition astm_aggregatetypedefinition;




    private List<astm_DefinitionObject> astm_definitionobjects;


    public astm_AggregateType(
    ) {
        super(
        );
        this.astm_definitionobjects = new ArrayList<>();
    }

    public astm_AggregateType(
        ArrayList<astm_DefinitionObject> astm_definitionobjects    ) {
        this.astm_definitionobjects = astm_definitionobjects;
    }


    public astm_AggregateTypeDefinition getAstm_aggregatetypedefinition() {
        return astm_aggregatetypedefinition;
    }

    public void setAstm_aggregatetypedefinition(astm_AggregateTypeDefinition astm_aggregatetypedefinition) {
        this.astm_aggregatetypedefinition = astm_aggregatetypedefinition;
    }
    public List<astm_DefinitionObject> getAstm_definitionobjects() {
        return astm_definitionobjects;
    }

    public void addAstm_definitionobject(Astm_definitionobject astm_definitionobject) {
        this.astm_definitionobjects.add(astm_definitionobject);
    }

}