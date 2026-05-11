





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ReconnectEdgeDescription extends MappingBasedToolDescription {

    private String reconnectionKind;





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

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}