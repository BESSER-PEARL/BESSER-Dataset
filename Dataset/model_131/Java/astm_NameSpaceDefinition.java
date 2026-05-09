





import java.util.List;
import java.util.ArrayList;

public class astm_NameSpaceDefinition extends DefinitionObject {






    private List<astm_DefinitionObject> astm_definitionobjects;




    private astm_Name astm_name;


    public astm_NameSpaceDefinition(
    ) {
        super(
        );
        this.astm_definitionobjects = new ArrayList<>();
    }

    public astm_NameSpaceDefinition(
        ArrayList<astm_DefinitionObject> astm_definitionobjects    ) {
        this.astm_definitionobjects = astm_definitionobjects;
    }


    public List<astm_DefinitionObject> getAstm_definitionobjects() {
        return astm_definitionobjects;
    }

    public void addAstm_definitionobject(Astm_definitionobject astm_definitionobject) {
        this.astm_definitionobjects.add(astm_definitionobject);
    }
    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }

}