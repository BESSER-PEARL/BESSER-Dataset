





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DNavigationLink  {

    private String label;
    private String targetType;





    private viewpoint_DNavigable viewpoint_dnavigable;


    public viewpoint_DNavigationLink(
        String label,        String targetType    ) {
        this.label = label;
        this.targetType = targetType;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getTargettype() {
        return targetType;
    }

    public void setTargettype(String targetType) {
        this.targetType = targetType;
    }

    public viewpoint_DNavigable getViewpoint_dnavigable() {
        return viewpoint_dnavigable;
    }

    public void setViewpoint_dnavigable(viewpoint_DNavigable viewpoint_dnavigable) {
        this.viewpoint_dnavigable = viewpoint_dnavigable;
    }

}