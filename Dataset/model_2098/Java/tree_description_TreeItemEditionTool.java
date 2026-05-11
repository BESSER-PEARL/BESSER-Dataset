





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemEditionTool extends TreeItemTool {






    private List<TreeItemMapping> treeitemmappings;


    public tree_description_TreeItemEditionTool(
    ) {
        super(
        );
        this.treeitemmappings = new ArrayList<>();
    }

    public tree_description_TreeItemEditionTool(
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