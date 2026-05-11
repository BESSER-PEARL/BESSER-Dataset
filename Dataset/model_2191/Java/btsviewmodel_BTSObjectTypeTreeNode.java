





import java.util.List;
import java.util.ArrayList;

public class btsviewmodel_BTSObjectTypeTreeNode  {

    private String value;
    private boolean selected;





    private btsviewmodel_BTSObjectTypeTreeNode btsviewmodel_btsobjecttypetreenode;




    private List<btsviewmodel_BTSObjectTypeTreeNode> btsviewmodel_btsobjecttypetreenodes;


    public btsviewmodel_BTSObjectTypeTreeNode(
        String value,        boolean selected    ) {
        this.value = value;
        this.selected = selected;
        this.btsviewmodel_btsobjecttypetreenodes = new ArrayList<>();
    }

    public btsviewmodel_BTSObjectTypeTreeNode(
        String value,        boolean selected        ArrayList<btsviewmodel_BTSObjectTypeTreeNode> btsviewmodel_btsobjecttypetreenodes    ) {
        this.value = value;
        this.selected = selected;
        this.btsviewmodel_btsobjecttypetreenodes = btsviewmodel_btsobjecttypetreenodes;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public btsviewmodel_BTSObjectTypeTreeNode getBtsviewmodel_btsobjecttypetreenode() {
        return btsviewmodel_btsobjecttypetreenode;
    }

    public void setBtsviewmodel_btsobjecttypetreenode(btsviewmodel_BTSObjectTypeTreeNode btsviewmodel_btsobjecttypetreenode) {
        this.btsviewmodel_btsobjecttypetreenode = btsviewmodel_btsobjecttypetreenode;
    }
    public List<btsviewmodel_BTSObjectTypeTreeNode> getBtsviewmodel_btsobjecttypetreenodes() {
        return btsviewmodel_btsobjecttypetreenodes;
    }

    public void addBtsviewmodel_btsobjecttypetreenode(Btsviewmodel_btsobjecttypetreenode btsviewmodel_btsobjecttypetreenode) {
        this.btsviewmodel_btsobjecttypetreenodes.add(btsviewmodel_btsobjecttypetreenode);
    }

}