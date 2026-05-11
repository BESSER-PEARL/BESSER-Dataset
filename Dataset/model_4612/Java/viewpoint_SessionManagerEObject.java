





import java.util.List;
import java.util.ArrayList;

public class viewpoint_SessionManagerEObject  {






    private List<viewpoint_DAnalysisSessionEObject> viewpoint_danalysissessioneobjects;


    public viewpoint_SessionManagerEObject(
    ) {
        this.viewpoint_danalysissessioneobjects = new ArrayList<>();
    }

    public viewpoint_SessionManagerEObject(
        ArrayList<viewpoint_DAnalysisSessionEObject> viewpoint_danalysissessioneobjects    ) {
        this.viewpoint_danalysissessioneobjects = viewpoint_danalysissessioneobjects;
    }


    public List<viewpoint_DAnalysisSessionEObject> getViewpoint_danalysissessioneobjects() {
        return viewpoint_danalysissessioneobjects;
    }

    public void addViewpoint_danalysissessioneobject(Viewpoint_danalysissessioneobject viewpoint_danalysissessioneobject) {
        this.viewpoint_danalysissessioneobjects.add(viewpoint_danalysissessioneobject);
    }

}