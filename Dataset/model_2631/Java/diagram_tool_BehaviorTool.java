





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_BehaviorTool extends AbstractToolDescription {

    private String domainClass;





    private tool_InitialOperation tool_initialoperation;


    public diagram_tool_BehaviorTool(
        String domainClass    ) {
        super(
        );
        this.domainClass = domainClass;
    }


    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }

    public tool_InitialOperation getTool_initialoperation() {
        return tool_initialoperation;
    }

    public void setTool_initialoperation(tool_InitialOperation tool_initialoperation) {
        this.tool_initialoperation = tool_initialoperation;
    }

}