





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ContainerModelOperation extends ModelOperation {






    private List<tool_ModelOperation> tool_modeloperations;


    public viewpoint_tool_ContainerModelOperation(
    ) {
        super(
        );
        this.tool_modeloperations = new ArrayList<>();
    }

    public viewpoint_tool_ContainerModelOperation(
        ArrayList<tool_ModelOperation> tool_modeloperations    ) {
        this.tool_modeloperations = tool_modeloperations;
    }


    public List<tool_ModelOperation> getTool_modeloperations() {
        return tool_modeloperations;
    }

    public void addTool_modeloperation(Tool_modeloperation tool_modeloperation) {
        this.tool_modeloperations.add(tool_modeloperation);
    }

}