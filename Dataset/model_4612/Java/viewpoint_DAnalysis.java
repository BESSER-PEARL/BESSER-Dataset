





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysis  {

    private String semanticResources;
    private String version;





    private viewpoint_DAnalysis viewpoint_danalysis;


    public viewpoint_DAnalysis(
        String semanticResources,        String version    ) {
        this.semanticResources = semanticResources;
        this.version = version;
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

    public viewpoint_DAnalysis getViewpoint_danalysis() {
        return viewpoint_danalysis;
    }

    public void setViewpoint_danalysis(viewpoint_DAnalysis viewpoint_danalysis) {
        this.viewpoint_danalysis = viewpoint_danalysis;
    }

}