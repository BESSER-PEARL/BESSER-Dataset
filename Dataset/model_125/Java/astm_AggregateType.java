





import java.util.List;
import java.util.ArrayList;

public class astm_AggregateType extends DataType {






    private List<DefinitionObject> definitionobjects;


    public astm_AggregateType(
    ) {
        super(
        );
        this.definitionobjects = new ArrayList<>();
    }

    public astm_AggregateType(
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