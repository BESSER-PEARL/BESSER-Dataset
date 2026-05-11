





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysis extends IdentifiedElement {

    private String version;
    private String semanticResources;





    private List<viewpoint_DView> viewpoint_dviews;




    private viewpoint_DAnalysis viewpoint_danalysis;




    private List<viewpoint_DView> viewpoint_dviews;




    private List<viewpoint_DFeatureExtension> viewpoint_dfeatureextensions;


    public viewpoint_DAnalysis(
        String version,        String semanticResources    ) {
        super(
        );
        this.version = version;
        this.semanticResources = semanticResources;
        this.viewpoint_dviews = new ArrayList<>();
        this.viewpoint_dviews = new ArrayList<>();
        this.viewpoint_dfeatureextensions = new ArrayList<>();
    }

    public viewpoint_DAnalysis(
        String version,        String semanticResources        ArrayList<viewpoint_DView> viewpoint_dviews,        ArrayList<viewpoint_DView> viewpoint_dviews,        ArrayList<viewpoint_DFeatureExtension> viewpoint_dfeatureextensions    ) {
        this.version = version;
        this.semanticResources = semanticResources;
        this.viewpoint_dviews = viewpoint_dviews;
        this.viewpoint_dviews = viewpoint_dviews;
        this.viewpoint_dfeatureextensions = viewpoint_dfeatureextensions;
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

    public List<viewpoint_DView> getViewpoint_dviews() {
        return viewpoint_dviews;
    }

    public void addViewpoint_dview(Viewpoint_dview viewpoint_dview) {
        this.viewpoint_dviews.add(viewpoint_dview);
    }
    public viewpoint_DAnalysis getViewpoint_danalysis() {
        return viewpoint_danalysis;
    }

    public void setViewpoint_danalysis(viewpoint_DAnalysis viewpoint_danalysis) {
        this.viewpoint_danalysis = viewpoint_danalysis;
    }
    public List<viewpoint_DView> getViewpoint_dviews() {
        return viewpoint_dviews;
    }

    public void addViewpoint_dview(Viewpoint_dview viewpoint_dview) {
        this.viewpoint_dviews.add(viewpoint_dview);
    }
    public List<viewpoint_DFeatureExtension> getViewpoint_dfeatureextensions() {
        return viewpoint_dfeatureextensions;
    }

    public void addViewpoint_dfeatureextension(Viewpoint_dfeatureextension viewpoint_dfeatureextension) {
        this.viewpoint_dfeatureextensions.add(viewpoint_dfeatureextension);
    }

}