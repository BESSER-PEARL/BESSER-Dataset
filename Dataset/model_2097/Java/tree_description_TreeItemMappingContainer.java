





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemMappingContainer  {






    private List<TreeItemMapping> treeitemmappings;




    private List<TreeItemContainerDropTool> treeitemcontainerdroptools;


    public tree_description_TreeItemMappingContainer(
    ) {
        this.treeitemmappings = new ArrayList<>();
        this.treeitemcontainerdroptools = new ArrayList<>();
    }

    public tree_description_TreeItemMappingContainer(
        ArrayList<TreeItemMapping> treeitemmappings,        ArrayList<TreeItemContainerDropTool> treeitemcontainerdroptools    ) {
        this.treeitemmappings = treeitemmappings;
        this.treeitemcontainerdroptools = treeitemcontainerdroptools;
    }


    public List<TreeItemMapping> getTreeitemmappings() {
        return treeitemmappings;
    }

    public void addTreeitemmapping(Treeitemmapping treeitemmapping) {
        this.treeitemmappings.add(treeitemmapping);
    }
    public List<TreeItemContainerDropTool> getTreeitemcontainerdroptools() {
        return treeitemcontainerdroptools;
    }

    public void addTreeitemcontainerdroptool(Treeitemcontainerdroptool treeitemcontainerdroptool) {
        this.treeitemcontainerdroptools.add(treeitemcontainerdroptool);
    }

}