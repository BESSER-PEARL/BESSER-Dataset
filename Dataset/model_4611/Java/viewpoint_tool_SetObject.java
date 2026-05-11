





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_SetObject extends ContainerModelOperation {

    private String featureName;





    private tool_viewpoint_EObject tool_viewpoint_eobject;


    public viewpoint_tool_SetObject(
        String featureName    ) {
        super(
        );
        this.featureName = featureName;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }

    public tool_viewpoint_EObject getTool_viewpoint_eobject() {
        return tool_viewpoint_eobject;
    }

    public void setTool_viewpoint_eobject(tool_viewpoint_EObject tool_viewpoint_eobject) {
        this.tool_viewpoint_eobject = tool_viewpoint_eobject;
    }

}