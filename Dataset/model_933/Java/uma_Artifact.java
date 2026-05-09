





import java.util.List;
import java.util.ArrayList;

public class uma_Artifact extends WorkProduct {

    private String group3;





    private List<uma_Artifact> uma_artifacts;


    public uma_Artifact(
        String group3    ) {
        super(
        );
        this.group3 = group3;
        this.uma_artifacts = new ArrayList<>();
    }

    public uma_Artifact(
        String group3        ArrayList<uma_Artifact> uma_artifacts    ) {
        this.group3 = group3;
        this.uma_artifacts = uma_artifacts;
    }

    public String getGroup3() {
        return group3;
    }

    public void setGroup3(String group3) {
        this.group3 = group3;
    }

    public List<uma_Artifact> getUma_artifacts() {
        return uma_artifacts;
    }

    public void addUma_artifact(Uma_artifact uma_artifact) {
        this.uma_artifacts.add(uma_artifact);
    }

}