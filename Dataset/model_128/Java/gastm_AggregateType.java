





import java.util.List;
import java.util.ArrayList;

public class gastm_AggregateType extends DataType {






    private List<DefinitionObject> definitionobjects;


    public gastm_AggregateType(
    ) {
        super(
        );
        this.definitionobjects = new ArrayList<>();
    }

    public gastm_AggregateType(
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