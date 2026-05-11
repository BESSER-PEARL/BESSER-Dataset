





import java.util.List;
import java.util.ArrayList;

public class notation_ExpandableNode extends Node {

    private boolean expanded;
    private String template;
    private boolean hasChildren;



    public notation_ExpandableNode(
        boolean expanded,        String template,        boolean hasChildren    ) {
        super(
        );
        this.expanded = expanded;
        this.template = template;
        this.hasChildren = hasChildren;
    }


    public boolean getExpanded() {
        return expanded;
    }

    public void setExpanded(boolean expanded) {
        this.expanded = expanded;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public boolean getHaschildren() {
        return hasChildren;
    }

    public void setHaschildren(boolean hasChildren) {
        this.hasChildren = hasChildren;
    }


}