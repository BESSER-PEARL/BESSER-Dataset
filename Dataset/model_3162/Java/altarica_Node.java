





import java.util.List;
import java.util.ArrayList;

public class altarica_Node extends AbstractDeclaration {

    private String name;
    private boolean isMain;





    private altarica_NodeInstanceDeclaration altarica_nodeinstancedeclaration;


    public altarica_Node(
        String name,        boolean isMain    ) {
        super(
        );
        this.name = name;
        this.isMain = isMain;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsmain() {
        return isMain;
    }

    public void setIsmain(boolean isMain) {
        this.isMain = isMain;
    }

    public altarica_NodeInstanceDeclaration getAltarica_nodeinstancedeclaration() {
        return altarica_nodeinstancedeclaration;
    }

    public void setAltarica_nodeinstancedeclaration(altarica_NodeInstanceDeclaration altarica_nodeinstancedeclaration) {
        this.altarica_nodeinstancedeclaration = altarica_nodeinstancedeclaration;
    }

}