





import java.util.List;
import java.util.ArrayList;

public class astm_sastm_DelphiWithStatement extends BlockStatement {






    private List<DefinitionObject> definitionobjects;


    public astm_sastm_DelphiWithStatement(
    ) {
        super(
        );
        this.definitionobjects = new ArrayList<>();
    }

    public astm_sastm_DelphiWithStatement(
        ArrayList<DefinitionObject> definitionobjects    ) {
        this.definitionobjects = definitionobjects;
    }


    public List<DefinitionObject> getDefinitionobjects() {
        return definitionobjects;
    }

    public void addDefinitionobject(Definitionobject definitionobject) {
        this.definitionobjects.add(definitionobject);
    }

}