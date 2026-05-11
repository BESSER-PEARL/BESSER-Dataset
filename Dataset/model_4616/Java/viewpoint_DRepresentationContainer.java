





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentationContainer extends DView {






    private List<viewpoint_EObject> viewpoint_eobjects;


    public viewpoint_DRepresentationContainer(
    ) {
        super(
        );
        this.viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_DRepresentationContainer(
        ArrayList<viewpoint_EObject> viewpoint_eobjects    ) {
        this.viewpoint_eobjects = viewpoint_eobjects;
    }


    public List<viewpoint_EObject> getViewpoint_eobjects() {
        return viewpoint_eobjects;
    }

    public void addViewpoint_eobject(Viewpoint_eobject viewpoint_eobject) {
        this.viewpoint_eobjects.add(viewpoint_eobject);
    }

}