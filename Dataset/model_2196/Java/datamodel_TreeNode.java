





import java.util.List;
import java.util.ArrayList;

public class datamodel_TreeNode  {






    private List<datamodel_TreeNode> datamodel_treenodes;




    private datamodel_TreeNode datamodel_treenode;


    public datamodel_TreeNode(
    ) {
        this.datamodel_treenodes = new ArrayList<>();
    }

    public datamodel_TreeNode(
        ArrayList<datamodel_TreeNode> datamodel_treenodes    ) {
        this.datamodel_treenodes = datamodel_treenodes;
    }


    public List<datamodel_TreeNode> getDatamodel_treenodes() {
        return datamodel_treenodes;
    }

    public void addDatamodel_treenode(Datamodel_treenode datamodel_treenode) {
        this.datamodel_treenodes.add(datamodel_treenode);
    }
    public datamodel_TreeNode getDatamodel_treenode() {
        return datamodel_treenode;
    }

    public void setDatamodel_treenode(datamodel_TreeNode datamodel_treenode) {
        this.datamodel_treenode = datamodel_treenode;
    }

}