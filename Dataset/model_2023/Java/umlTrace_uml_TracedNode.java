





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedNode extends uml_TracedDeploymentTarget, uml_TracedClass {






    private List<uml_TracedNode> uml_tracednodes;


    public umlTrace_uml_TracedNode(
    ) {
        super(
        );
        this.uml_tracednodes = new ArrayList<>();
    }

    public umlTrace_uml_TracedNode(
        ArrayList<uml_TracedNode> uml_tracednodes    ) {
        this.uml_tracednodes = uml_tracednodes;
    }


    public List<uml_TracedNode> getUml_tracednodes() {
        return uml_tracednodes;
    }

    public void addUml_tracednode(Uml_tracednode uml_tracednode) {
        this.uml_tracednodes.add(uml_tracednode);
    }

}