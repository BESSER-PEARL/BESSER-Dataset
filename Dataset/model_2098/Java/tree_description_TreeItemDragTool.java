





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemDragTool extends tool_MappingBasedToolDescription, description_TreeItemTool {

    private String dragSourceType;



    public tree_description_TreeItemDragTool(
        String dragSourceType    ) {
        super(
        );
        this.dragSourceType = dragSourceType;
    }


    public String getDragsourcetype() {
        return dragSourceType;
    }

    public void setDragsourcetype(String dragSourceType) {
        this.dragSourceType = dragSourceType;
    }


}