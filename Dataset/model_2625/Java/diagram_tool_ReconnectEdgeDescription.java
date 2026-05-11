





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_ReconnectEdgeDescription extends MappingBasedToolDescription {

    private String reconnectionKind;



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


}