





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_DeleteHook  {

    private String id;





    private List<tool_DeleteHookParameter> tool_deletehookparameters;


    public diagram_tool_DeleteHook(
        String id    ) {
        this.id = id;
        this.tool_deletehookparameters = new ArrayList<>();
    }

    public diagram_tool_DeleteHook(
        String id        ArrayList<tool_DeleteHookParameter> tool_deletehookparameters    ) {
        this.id = id;
        this.tool_deletehookparameters = tool_deletehookparameters;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<tool_DeleteHookParameter> getTool_deletehookparameters() {
        return tool_deletehookparameters;
    }

    public void addTool_deletehookparameter(Tool_deletehookparameter tool_deletehookparameter) {
        this.tool_deletehookparameters.add(tool_deletehookparameter);
    }

}