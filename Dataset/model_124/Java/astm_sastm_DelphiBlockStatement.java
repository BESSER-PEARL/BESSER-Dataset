





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_DelphiBlockStatement extends BlockStatement {






    private List<NamedTypeReference> namedtypereferences;




    private List<DefinitionObject> definitionobjects;


    public astm_sastm_DelphiBlockStatement(
    ) {
        super(
        );
        this.namedtypereferences = new ArrayList<>();
        this.definitionobjects = new ArrayList<>();
    }

    public astm_sastm_DelphiBlockStatement(
        ArrayList<NamedTypeReference> namedtypereferences,        ArrayList<DefinitionObject> definitionobjects    ) {
        this.namedtypereferences = namedtypereferences;
        this.definitionobjects = definitionobjects;
    }


    public List<NamedTypeReference> getNamedtypereferences() {
        return namedtypereferences;
    }

    public void addNamedtypereference(Namedtypereference namedtypereference) {
        this.namedtypereferences.add(namedtypereference);
    }
    public List<DefinitionObject> getDefinitionobjects() {
        return definitionobjects;
    }

    public void addDefinitionobject(Definitionobject definitionobject) {
        this.definitionobjects.add(definitionobject);
    }

}