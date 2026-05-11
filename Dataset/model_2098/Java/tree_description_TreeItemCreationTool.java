





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemCreationTool extends tool_MappingBasedToolDescription, description_TreeItemTool {






    private List<TreeItemMapping> treeitemmappings;


    public tree_description_TreeItemCreationTool(
    ) {
        super(
        );
        this.treeitemmappings = new ArrayList<>();
    }

    public tree_description_TreeItemCreationTool(
        ArrayList<TreeItemMapping> treeitemmappings    ) {
        this.treeitemmappings = treeitemmappings;
    }


    public List<TreeItemMapping> getTreeitemmappings() {
        return treeitemmappings;
    }

    public void addTreeitemmapping(Treeitemmapping treeitemmapping) {
        this.treeitemmappings.add(treeitemmapping);
    }

}