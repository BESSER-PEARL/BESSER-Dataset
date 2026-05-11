





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentationElement extends DSemanticDecorator, DStylizable, DMappingBased, DRefreshable {

    private String name;





    private List<viewpoint_EObject> viewpoint_eobjects;


    public viewpoint_DRepresentationElement(
        String name    ) {
        super(
        );
        this.name = name;
        this.viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_DRepresentationElement(
        String name        ArrayList<viewpoint_EObject> viewpoint_eobjects    ) {
        this.name = name;
        this.viewpoint_eobjects = viewpoint_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<viewpoint_EObject> getViewpoint_eobjects() {
        return viewpoint_eobjects;
    }

    public void addViewpoint_eobject(Viewpoint_eobject viewpoint_eobject) {
        this.viewpoint_eobjects.add(viewpoint_eobject);
    }

}