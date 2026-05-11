





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentationDescriptor  {

    private String name;





    private viewpoint_DView viewpoint_dview;




    private viewpoint_EObject viewpoint_eobject;


    public viewpoint_DRepresentationDescriptor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public viewpoint_DView getViewpoint_dview() {
        return viewpoint_dview;
    }

    public void setViewpoint_dview(viewpoint_DView viewpoint_dview) {
        this.viewpoint_dview = viewpoint_dview;
    }
    public viewpoint_EObject getViewpoint_eobject() {
        return viewpoint_eobject;
    }

    public void setViewpoint_eobject(viewpoint_EObject viewpoint_eobject) {
        this.viewpoint_eobject = viewpoint_eobject;
    }

}