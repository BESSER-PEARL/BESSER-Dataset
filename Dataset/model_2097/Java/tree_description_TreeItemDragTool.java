





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemDragTool extends description_TreeItemTool, tool_MappingBasedToolDescription {

    private String dragSourceType;





    private List<TreeItemMappingContainer> treeitemmappingcontainers;




    private PrecedingSiblingsVariables precedingsiblingsvariables;




    private tool_ContainerViewVariable tool_containerviewvariable;


    public tree_description_TreeItemDragTool(
        String dragSourceType    ) {
        super(
        );
        this.dragSourceType = dragSourceType;
        this.treeitemmappingcontainers = new ArrayList<>();
    }

    public tree_description_TreeItemDragTool(
        String dragSourceType        ArrayList<TreeItemMappingContainer> treeitemmappingcontainers    ) {
        this.dragSourceType = dragSourceType;
        this.treeitemmappingcontainers = treeitemmappingcontainers;
    }

    public String getDragsourcetype() {
        return dragSourceType;
    }

    public void setDragsourcetype(String dragSourceType) {
        this.dragSourceType = dragSourceType;
    }

    public List<TreeItemMappingContainer> getTreeitemmappingcontainers() {
        return treeitemmappingcontainers;
    }

    public void addTreeitemmappingcontainer(Treeitemmappingcontainer treeitemmappingcontainer) {
        this.treeitemmappingcontainers.add(treeitemmappingcontainer);
    }
    public PrecedingSiblingsVariables getPrecedingsiblingsvariables() {
        return precedingsiblingsvariables;
    }

    public void setPrecedingsiblingsvariables(PrecedingSiblingsVariables precedingsiblingsvariables) {
        this.precedingsiblingsvariables = precedingsiblingsvariables;
    }
    public tool_ContainerViewVariable getTool_containerviewvariable() {
        return tool_containerviewvariable;
    }

    public void setTool_containerviewvariable(tool_ContainerViewVariable tool_containerviewvariable) {
        this.tool_containerviewvariable = tool_containerviewvariable;
    }

}