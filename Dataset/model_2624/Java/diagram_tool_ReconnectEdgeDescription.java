





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ReconnectEdgeDescription extends MappingBasedToolDescription {

    private String reconnectionKind;





    private tool_TargetEdgeCreationVariable tool_targetedgecreationvariable;




    private tool_SourceEdgeCreationVariable tool_sourceedgecreationvariable;




    private tool_InitialOperation tool_initialoperation;


    public diagram_tool_ReconnectEdgeDescription(
        String reconnectionKind    ) {
        super(
        );
        this.reconnectionKind = reconnectionKind;
    }


    public String getReconnectionkind() {
        return reconnectionKind;
    }

    public void setReconnectionkind(String reconnectionKind) {
        this.reconnectionKind = reconnectionKind;
    }

    public tool_TargetEdgeCreationVariable getTool_targetedgecreationvariable() {
        return tool_targetedgecreationvariable;
    }

    public void setTool_targetedgecreationvariable(tool_TargetEdgeCreationVariable tool_targetedgecreationvariable) {
        this.tool_targetedgecreationvariable = tool_targetedgecreationvariable;
    }
    public tool_SourceEdgeCreationVariable getTool_sourceedgecreationvariable() {
        return tool_sourceedgecreationvariable;
    }

    public void setTool_sourceedgecreationvariable(tool_SourceEdgeCreationVariable tool_sourceedgecreationvariable) {
        this.tool_sourceedgecreationvariable = tool_sourceedgecreationvariable;
    }
    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}