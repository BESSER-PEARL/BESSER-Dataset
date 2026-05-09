





import java.util.List;
import java.util.ArrayList;

public class uma_Artifact extends WorkProduct {






    private List<uma_Artifact> uma_artifacts;




    private uma_Artifact uma_artifact;


    public uma_Artifact(
    ) {
        super(
        );
        this.uma_artifacts = new ArrayList<>();
    }

    public uma_Artifact(
        ArrayList<uma_Artifact> uma_artifacts    ) {
        this.uma_artifacts = uma_artifacts;
    }


    public List<uma_Artifact> getUma_artifacts() {
        return uma_artifacts;
    }

    public void addUma_artifact(Uma_artifact uma_artifact) {
        this.uma_artifacts.add(uma_artifact);
    }
    public uma_Artifact getUma_artifact() {
        return uma_artifact;
    }

    public void setUma_artifact(uma_Artifact uma_artifact) {
        this.uma_artifact = uma_artifact;
    }

}