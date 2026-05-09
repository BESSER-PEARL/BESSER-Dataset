





import java.util.List;
import java.util.ArrayList;

public class gastm_NameReference extends Expression {






    private DefinitionObject definitionobject;




    private Name name;


    public gastm_NameReference(
    ) {
        super(
        );
    }



    public DefinitionObject getDefinitionobject() {
        return definitionobject;
    }

    public void setDefinitionobject(DefinitionObject definitionobject) {
        this.definitionobject = definitionobject;
    }
    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }

}