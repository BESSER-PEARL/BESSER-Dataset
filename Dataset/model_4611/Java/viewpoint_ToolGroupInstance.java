





import java.util.List;
import java.util.ArrayList;

public class viewpoint_ToolGroupInstance extends ToolInstance {






    private List<viewpoint_ToolInstance> viewpoint_toolinstances;




    private viewpoint_EObject viewpoint_eobject;


    public viewpoint_ToolGroupInstance(
    ) {
        super(
        );
        this.viewpoint_toolinstances = new ArrayList<>();
    }

    public viewpoint_ToolGroupInstance(
        ArrayList<viewpoint_ToolInstance> viewpoint_toolinstances    ) {
        this.viewpoint_toolinstances = viewpoint_toolinstances;
    }


    public List<viewpoint_ToolInstance> getViewpoint_toolinstances() {
        return viewpoint_toolinstances;
    }

    public void addViewpoint_toolinstance(Viewpoint_toolinstance viewpoint_toolinstance) {
        this.viewpoint_toolinstances.add(viewpoint_toolinstance);
    }
    public viewpoint_EObject getViewpoint_eobject() {
        return viewpoint_eobject;
    }

    public void setViewpoint_eobject(viewpoint_EObject viewpoint_eobject) {
        this.viewpoint_eobject = viewpoint_eobject;
    }

}