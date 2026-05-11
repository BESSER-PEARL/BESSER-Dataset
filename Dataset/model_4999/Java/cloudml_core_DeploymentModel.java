





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_DeploymentModel extends WithProperties {






    private List<NodeInstance> nodeinstances;




    private List<ArtefactInstance> artefactinstances;


    public cloudml_core_DeploymentModel(
    ) {
        super(
        );
        this.nodeinstances = new ArrayList<>();
        this.artefactinstances = new ArrayList<>();
    }

    public cloudml_core_DeploymentModel(
        ArrayList<NodeInstance> nodeinstances,        ArrayList<ArtefactInstance> artefactinstances    ) {
        this.nodeinstances = nodeinstances;
        this.artefactinstances = artefactinstances;
    }


    public List<NodeInstance> getNodeinstances() {
        return nodeinstances;
    }

    public void addNodeinstance(Nodeinstance nodeinstance) {
        this.nodeinstances.add(nodeinstance);
    }
    public List<ArtefactInstance> getArtefactinstances() {
        return artefactinstances;
    }

    public void addArtefactinstance(Artefactinstance artefactinstance) {
        this.artefactinstances.add(artefactinstance);
    }

}