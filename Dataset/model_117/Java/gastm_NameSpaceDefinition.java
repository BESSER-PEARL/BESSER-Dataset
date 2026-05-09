





import java.util.List;
import java.util.ArrayList;

public class gastm_NameSpaceDefinition extends DefinitionObject {






    private gastm_Name gastm_name;




    private List<gastm_DefinitionObject> gastm_definitionobjects;


    public gastm_NameSpaceDefinition(
    ) {
        super(
        );
        this.gastm_definitionobjects = new ArrayList<>();
    }

    public gastm_NameSpaceDefinition(
        ArrayList<gastm_DefinitionObject> gastm_definitionobjects    ) {
        this.gastm_definitionobjects = gastm_definitionobjects;
    }


    public gastm_Name getGastm_name() {
        return gastm_name;
    }

    public void setGastm_name(gastm_Name gastm_name) {
        this.gastm_name = gastm_name;
    }
    public List<gastm_DefinitionObject> getGastm_definitionobjects() {
        return gastm_definitionobjects;
    }

    public void addGastm_definitionobject(Gastm_definitionobject gastm_definitionobject) {
        this.gastm_definitionobjects.add(gastm_definitionobject);
    }

}