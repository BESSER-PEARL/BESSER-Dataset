





import java.util.List;
import java.util.ArrayList;

public class diagram_tool_BehaviorTool extends AbstractToolDescription {

    private String domainClass;



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


}