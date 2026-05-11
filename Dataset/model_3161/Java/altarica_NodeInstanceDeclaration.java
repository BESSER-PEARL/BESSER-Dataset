





import java.util.List;
import java.util.ArrayList;

public class altarica_NodeInstanceDeclaration  {






    private altarica_Node altarica_node;




    private List<altarica_NodeInstance> altarica_nodeinstances;




    private altarica_NodeInstanceSpecification altarica_nodeinstancespecification;


    public altarica_NodeInstanceDeclaration(
    ) {
        this.altarica_nodeinstances = new ArrayList<>();
    }

    public altarica_NodeInstanceDeclaration(
        ArrayList<altarica_NodeInstance> altarica_nodeinstances    ) {
        this.altarica_nodeinstances = altarica_nodeinstances;
    }


    public altarica_Node getAltarica_node() {
        return altarica_node;
    }

    public void setAltarica_node(altarica_Node altarica_node) {
        this.altarica_node = altarica_node;
    }
    public List<altarica_NodeInstance> getAltarica_nodeinstances() {
        return altarica_nodeinstances;
    }

    public void addAltarica_nodeinstance(Altarica_nodeinstance altarica_nodeinstance) {
        this.altarica_nodeinstances.add(altarica_nodeinstance);
    }
    public altarica_NodeInstanceSpecification getAltarica_nodeinstancespecification() {
        return altarica_nodeinstancespecification;
    }

    public void setAltarica_nodeinstancespecification(altarica_NodeInstanceSpecification altarica_nodeinstancespecification) {
        this.altarica_nodeinstancespecification = altarica_nodeinstancespecification;
    }

}