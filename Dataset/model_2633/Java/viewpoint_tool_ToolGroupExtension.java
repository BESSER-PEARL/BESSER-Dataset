





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ToolGroupExtension  {






    private List<tool_AbstractToolDescription> tool_abstracttooldescriptions;


    public viewpoint_tool_ToolGroupExtension(
    ) {
        this.tool_abstracttooldescriptions = new ArrayList<>();
    }

    public viewpoint_tool_ToolGroupExtension(
        ArrayList<tool_AbstractToolDescription> tool_abstracttooldescriptions    ) {
        this.tool_abstracttooldescriptions = tool_abstracttooldescriptions;
    }


    public List<tool_AbstractToolDescription> getTool_abstracttooldescriptions() {
        return tool_abstracttooldescriptions;
    }

    public void addTool_abstracttooldescription(Tool_abstracttooldescription tool_abstracttooldescription) {
        this.tool_abstracttooldescriptions.add(tool_abstracttooldescription);
    }

}