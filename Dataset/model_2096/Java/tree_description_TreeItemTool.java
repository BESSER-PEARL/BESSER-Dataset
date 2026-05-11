





import java.util.List;
import java.util.ArrayList;

public class tree_description_TreeItemTool extends AbstractToolDescription {






    private tool_ModelOperation tool_modeloperation;




    private List<TreeVariable> treevariables;


    public tree_description_TreeItemTool(
    ) {
        super(
        );
        this.treevariables = new ArrayList<>();
    }

    public tree_description_TreeItemTool(
        ArrayList<TreeVariable> treevariables    ) {
        this.treevariables = treevariables;
    }


    public tool_ModelOperation getTool_modeloperation() {
        return tool_modeloperation;
    }

    public void setTool_modeloperation(tool_ModelOperation tool_modeloperation) {
        this.tool_modeloperation = tool_modeloperation;
    }
    public List<TreeVariable> getTreevariables() {
        return treevariables;
    }

    public void addTreevariable(Treevariable treevariable) {
        this.treevariables.add(treevariable);
    }

}