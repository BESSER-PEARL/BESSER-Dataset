





import java.util.List;
import java.util.ArrayList;

public class astm_NameReference extends Expression {






    private Name name;




    private DefinitionObject definitionobject;


    public astm_NameReference(
    ) {
        super(
        );
    }



    public Name getName() {
        return name;
    }

    public void setName(Name name) {
        this.name = name;
    }
    public DefinitionObject getDefinitionobject() {
        return definitionobject;
    }

    public void setDefinitionobject(DefinitionObject definitionobject) {
        this.definitionobject = definitionobject;
    }

}