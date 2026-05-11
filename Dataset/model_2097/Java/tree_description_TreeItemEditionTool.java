





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemEditionTool extends TreeItemTool {






    private tool_ElementDropVariable tool_elementdropvariable;




    private List<TreeItemMapping> treeitemmappings;




    private tool_ElementDropVariable tool_elementdropvariable;


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


    public tool_ElementDropVariable getTool_elementdropvariable() {
        return tool_elementdropvariable;
    }

    public void setTool_elementdropvariable(tool_ElementDropVariable tool_elementdropvariable) {
        this.tool_elementdropvariable = tool_elementdropvariable;
    }
    public List<TreeItemMapping> getTreeitemmappings() {
        return treeitemmappings;
    }

    public void addTreeitemmapping(Treeitemmapping treeitemmapping) {
        this.treeitemmappings.add(treeitemmapping);
    }
    public tool_ElementDropVariable getTool_elementdropvariable() {
        return tool_elementdropvariable;
    }

    public void setTool_elementdropvariable(tool_ElementDropVariable tool_elementdropvariable) {
        this.tool_elementdropvariable = tool_elementdropvariable;
    }

}