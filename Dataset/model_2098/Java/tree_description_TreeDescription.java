





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeDescription extends description_RepresentationDescription, description_TreeItemMappingContainer {

    private String preconditionExpression;
    private String domainClass;





    private List<tool_RepresentationNavigationDescription> tool_representationnavigationdescriptions;


    public tree_description_TreeDescription(
        String preconditionExpression,        String domainClass    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.tool_representationnavigationdescriptions = new ArrayList<>();
    }

    public tree_description_TreeDescription(
        String preconditionExpression,        String domainClass        ArrayList<tool_RepresentationNavigationDescription> tool_representationnavigationdescriptions    ) {
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.tool_representationnavigationdescriptions = tool_representationnavigationdescriptions;
    }

    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }

    public List<tool_RepresentationNavigationDescription> getTool_representationnavigationdescriptions() {
        return tool_representationnavigationdescriptions;
    }

    public void addTool_representationnavigationdescription(Tool_representationnavigationdescription tool_representationnavigationdescription) {
        this.tool_representationnavigationdescriptions.add(tool_representationnavigationdescription);
    }

}