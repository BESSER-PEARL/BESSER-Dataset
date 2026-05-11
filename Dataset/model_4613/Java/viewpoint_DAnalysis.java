





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysis  {

    private String semanticResources;
    private String version;





    private List<viewpoint_DAnalysis> viewpoint_danalysiss;


    public viewpoint_DAnalysis(
        String semanticResources,        String version    ) {
        this.semanticResources = semanticResources;
        this.version = version;
        this.viewpoint_danalysiss = new ArrayList<>();
    }

    public viewpoint_DAnalysis(
        String semanticResources,        String version        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss    ) {
        this.semanticResources = semanticResources;
        this.version = version;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
    }

    public String getSemanticresources() {
        return semanticResources;
    }

    public void setSemanticresources(String semanticResources) {
        this.semanticResources = semanticResources;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<viewpoint_DAnalysis> getViewpoint_danalysiss() {
        return viewpoint_danalysiss;
    }

    public void addViewpoint_danalysis(Viewpoint_danalysis viewpoint_danalysis) {
        this.viewpoint_danalysiss.add(viewpoint_danalysis);
    }

}