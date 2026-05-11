





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysis  {

    private String semanticResources;
    private String version;





    private List<viewpoint_EObject> viewpoint_eobjects;




    private List<viewpoint_DView> viewpoint_dviews;




    private List<DAnnotationEntry> dannotationentrys;




    private List<viewpoint_DView> viewpoint_dviews;




    private viewpoint_DAnalysis viewpoint_danalysis;


    public viewpoint_DAnalysis(
        String semanticResources,        String version    ) {
        this.semanticResources = semanticResources;
        this.version = version;
        this.viewpoint_eobjects = new ArrayList<>();
        this.viewpoint_dviews = new ArrayList<>();
        this.dannotationentrys = new ArrayList<>();
        this.viewpoint_dviews = new ArrayList<>();
    }

    public viewpoint_DAnalysis(
        String semanticResources,        String version        ArrayList<viewpoint_EObject> viewpoint_eobjects,        ArrayList<viewpoint_DView> viewpoint_dviews,        ArrayList<DAnnotationEntry> dannotationentrys,        ArrayList<viewpoint_DView> viewpoint_dviews    ) {
        this.semanticResources = semanticResources;
        this.version = version;
        this.viewpoint_eobjects = viewpoint_eobjects;
        this.viewpoint_dviews = viewpoint_dviews;
        this.dannotationentrys = dannotationentrys;
        this.viewpoint_dviews = viewpoint_dviews;
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

    public List<viewpoint_EObject> getViewpoint_eobjects() {
        return viewpoint_eobjects;
    }

    public void addViewpoint_eobject(Viewpoint_eobject viewpoint_eobject) {
        this.viewpoint_eobjects.add(viewpoint_eobject);
    }
    public List<viewpoint_DView> getViewpoint_dviews() {
        return viewpoint_dviews;
    }

    public void addViewpoint_dview(Viewpoint_dview viewpoint_dview) {
        this.viewpoint_dviews.add(viewpoint_dview);
    }
    public List<DAnnotationEntry> getDannotationentrys() {
        return dannotationentrys;
    }

    public void addDannotationentry(Dannotationentry dannotationentry) {
        this.dannotationentrys.add(dannotationentry);
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

}