





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemContainerDropTool extends tool_MappingBasedToolDescription, description_TreeItemTool {

    private String dragSource;



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


}