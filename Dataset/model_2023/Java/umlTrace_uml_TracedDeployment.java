





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedDeployment extends TracedDependency {






    private uml_TracedDeploymentTarget uml_traceddeploymenttarget;




    private List<uml_TracedDeployedArtifact> uml_traceddeployedartifacts;


    public umlTrace_uml_TracedDeployment(
    ) {
        super(
        );
        this.uml_traceddeployedartifacts = new ArrayList<>();
    }

    public umlTrace_uml_TracedDeployment(
        ArrayList<uml_TracedDeployedArtifact> uml_traceddeployedartifacts    ) {
        this.uml_traceddeployedartifacts = uml_traceddeployedartifacts;
    }


    public uml_TracedDeploymentTarget getUml_traceddeploymenttarget() {
        return uml_traceddeploymenttarget;
    }

    public void setUml_traceddeploymenttarget(uml_TracedDeploymentTarget uml_traceddeploymenttarget) {
        this.uml_traceddeploymenttarget = uml_traceddeploymenttarget;
    }
    public List<uml_TracedDeployedArtifact> getUml_traceddeployedartifacts() {
        return uml_traceddeployedartifacts;
    }

    public void addUml_traceddeployedartifact(Uml_traceddeployedartifact uml_traceddeployedartifact) {
        this.uml_traceddeployedartifacts.add(uml_traceddeployedartifact);
    }

}