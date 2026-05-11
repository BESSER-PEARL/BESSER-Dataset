





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemContainerDropTool extends description_TreeItemTool, tool_MappingBasedToolDescription {

    private String dragSource;





    private tool_ContainerViewVariable tool_containerviewvariable;




    private PrecedingSiblingsVariables precedingsiblingsvariables;


    public tree_description_TreeItemContainerDropTool(
        String dragSource    ) {
        super(
        );
        this.dragSource = dragSource;
    }


    public String getDragsource() {
        return dragSource;
    }

    public void setDragsource(String dragSource) {
        this.dragSource = dragSource;
    }

    public tool_ContainerViewVariable getTool_containerviewvariable() {
        return tool_containerviewvariable;
    }

    public void setTool_containerviewvariable(tool_ContainerViewVariable tool_containerviewvariable) {
        this.tool_containerviewvariable = tool_containerviewvariable;
    }
    public PrecedingSiblingsVariables getPrecedingsiblingsvariables() {
        return precedingsiblingsvariables;
    }

    public void setPrecedingsiblingsvariables(PrecedingSiblingsVariables precedingsiblingsvariables) {
        this.precedingsiblingsvariables = precedingsiblingsvariables;
    }

}