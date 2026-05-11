





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedDeploymentTarget extends TracedNamedElement {






    private List<uml_TracedDeployment> uml_traceddeployments;


    public umlTrace_uml_TracedDeploymentTarget(
    ) {
        super(
        );
        this.uml_traceddeployments = new ArrayList<>();
    }

    public umlTrace_uml_TracedDeploymentTarget(
        ArrayList<uml_TracedDeployment> uml_traceddeployments    ) {
        this.uml_traceddeployments = uml_traceddeployments;
    }


    public List<uml_TracedDeployment> getUml_traceddeployments() {
        return uml_traceddeployments;
    }

    public void addUml_traceddeployment(Uml_traceddeployment uml_traceddeployment) {
        this.uml_traceddeployments.add(uml_traceddeployment);
    }

}