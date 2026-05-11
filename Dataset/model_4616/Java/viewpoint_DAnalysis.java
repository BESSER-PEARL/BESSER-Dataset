





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DAnalysis  {

    private String version;





    private List<viewpoint_DAnalysis> viewpoint_danalysiss;




    private List<viewpoint_DFeatureExtension> viewpoint_dfeatureextensions;


    public viewpoint_DAnalysis(
        String version    ) {
        this.version = version;
        this.viewpoint_danalysiss = new ArrayList<>();
        this.viewpoint_dfeatureextensions = new ArrayList<>();
    }

    public viewpoint_DAnalysis(
        String version        ArrayList<viewpoint_DAnalysis> viewpoint_danalysiss,        ArrayList<viewpoint_DFeatureExtension> viewpoint_dfeatureextensions    ) {
        this.version = version;
        this.viewpoint_danalysiss = viewpoint_danalysiss;
        this.viewpoint_dfeatureextensions = viewpoint_dfeatureextensions;
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
    public List<viewpoint_DFeatureExtension> getViewpoint_dfeatureextensions() {
        return viewpoint_dfeatureextensions;
    }

    public void addViewpoint_dfeatureextension(Viewpoint_dfeatureextension viewpoint_dfeatureextension) {
        this.viewpoint_dfeatureextensions.add(viewpoint_dfeatureextension);
    }

}