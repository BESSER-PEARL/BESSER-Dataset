





import java.util.List;
import java.util.ArrayList;

public class gremlin_VariableAccess extends TraversalElement {

    private String name;





    private gremlin_TypeDeclaration gremlin_typedeclaration;


    public gremlin_VariableAccess(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gremlin_TypeDeclaration getGremlin_typedeclaration() {
        return gremlin_typedeclaration;
    }

    public void setGremlin_typedeclaration(gremlin_TypeDeclaration gremlin_typedeclaration) {
        this.gremlin_typedeclaration = gremlin_typedeclaration;
    }

}