





import java.util.List;
import java.util.ArrayList;

public class gastm_Scope extends GASTMSemanticObject {






    private gastm_Scope gastm_scope;




    private List<gastm_DefinitionObject> gastm_definitionobjects;


    public gastm_Scope(
    ) {
        super(
        );
        this.gastm_definitionobjects = new ArrayList<>();
    }

    public gastm_Scope(
        ArrayList<gastm_DefinitionObject> gastm_definitionobjects    ) {
        this.gastm_definitionobjects = gastm_definitionobjects;
    }


    public gastm_Scope getGastm_scope() {
        return gastm_scope;
    }

    public void setGastm_scope(gastm_Scope gastm_scope) {
        this.gastm_scope = gastm_scope;
    }
    public List<gastm_DefinitionObject> getGastm_definitionobjects() {
        return gastm_definitionobjects;
    }

    public void addGastm_definitionobject(Gastm_definitionobject gastm_definitionobject) {
        this.gastm_definitionobjects.add(gastm_definitionobject);
    }

}