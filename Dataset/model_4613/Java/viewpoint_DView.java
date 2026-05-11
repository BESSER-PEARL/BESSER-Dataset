





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DView extends DRefreshable {






    private viewpoint_DAnalysis viewpoint_danalysis;




    private viewpoint_DAnalysis viewpoint_danalysis;




    private List<viewpoint_EObject> viewpoint_eobjects;


    public viewpoint_DView(
    ) {
        super(
        );
        this.viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_DView(
        ArrayList<viewpoint_EObject> viewpoint_eobjects    ) {
        this.viewpoint_eobjects = viewpoint_eobjects;
    }


    public viewpoint_DAnalysis getViewpoint_danalysis() {
        return viewpoint_danalysis;
    }

    public void setViewpoint_danalysis(viewpoint_DAnalysis viewpoint_danalysis) {
        this.viewpoint_danalysis = viewpoint_danalysis;
    }
    public viewpoint_DAnalysis getViewpoint_danalysis() {
        return viewpoint_danalysis;
    }

    public void setViewpoint_danalysis(viewpoint_DAnalysis viewpoint_danalysis) {
        this.viewpoint_danalysis = viewpoint_danalysis;
    }
    public List<viewpoint_EObject> getViewpoint_eobjects() {
        return viewpoint_eobjects;
    }

    public void addViewpoint_eobject(Viewpoint_eobject viewpoint_eobject) {
        this.viewpoint_eobjects.add(viewpoint_eobject);
    }

}