





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysis  {

    private String version;
    private String semanticResources;





    private List<viewpoint_DAnalysis> viewpoint_danalysiss;


    public viewpoint_DAnalysis(
        String version,        String semanticResources    ) {
        this.version = version;
        this.semanticResources = semanticResources;
        this.viewpoint_danalysiss = new ArrayList<>();
    }

    public viewpoint_DAnalysis(
        String version,        String semanticResources        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss    ) {
        this.version = version;
        this.semanticResources = semanticResources;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getSemanticresources() {
        return semanticResources;
    }

    public void setSemanticresources(String semanticResources) {
        this.semanticResources = semanticResources;
    }

    public List<viewpoint_DAnalysis> getViewpoint_danalysiss() {
        return viewpoint_danalysiss;
    }

    public void addViewpoint_danalysis(Viewpoint_danalysis viewpoint_danalysis) {
        this.viewpoint_danalysiss.add(viewpoint_danalysis);
    }

}