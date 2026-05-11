





import java.util.List;
import java.util.ArrayList;

public class description_AbstractNodeMapping  {






    private viewpoint_description_EdgeMapping viewpoint_description_edgemapping;




    private viewpoint_tool_NodeCreationDescription viewpoint_tool_nodecreationdescription;




    private viewpoint_tool_ContainerCreationDescription viewpoint_tool_containercreationdescription;


    public description_AbstractNodeMapping(
    ) {
    }



    public viewpoint_description_EdgeMapping getViewpoint_description_edgemapping() {
        return viewpoint_description_edgemapping;
    }

    public void setViewpoint_description_edgemapping(viewpoint_description_EdgeMapping viewpoint_description_edgemapping) {
        this.viewpoint_description_edgemapping = viewpoint_description_edgemapping;
    }
    public viewpoint_tool_NodeCreationDescription getViewpoint_tool_nodecreationdescription() {
        return viewpoint_tool_nodecreationdescription;
    }

    public void setViewpoint_tool_nodecreationdescription(viewpoint_tool_NodeCreationDescription viewpoint_tool_nodecreationdescription) {
        this.viewpoint_tool_nodecreationdescription = viewpoint_tool_nodecreationdescription;
    }
    public viewpoint_tool_ContainerCreationDescription getViewpoint_tool_containercreationdescription() {
        return viewpoint_tool_containercreationdescription;
    }

    public void setViewpoint_tool_containercreationdescription(viewpoint_tool_ContainerCreationDescription viewpoint_tool_containercreationdescription) {
        this.viewpoint_tool_containercreationdescription = viewpoint_tool_containercreationdescription;
    }

}