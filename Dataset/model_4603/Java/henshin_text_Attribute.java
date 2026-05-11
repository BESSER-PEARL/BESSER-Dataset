





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Attribute  {

    private String update;
    private String actiontype;





    private henshin_text_MultiRuleReuseNode henshin_text_multirulereusenode;




    private henshin_text_Node henshin_text_node;


    public henshin_text_Attribute(
        String update,        String actiontype    ) {
        this.update = update;
        this.actiontype = actiontype;
    }


    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }
    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }

    public henshin_text_MultiRuleReuseNode getHenshin_text_multirulereusenode() {
        return henshin_text_multirulereusenode;
    }

    public void setHenshin_text_multirulereusenode(henshin_text_MultiRuleReuseNode henshin_text_multirulereusenode) {
        this.henshin_text_multirulereusenode = henshin_text_multirulereusenode;
    }
    public henshin_text_Node getHenshin_text_node() {
        return henshin_text_node;
    }

    public void setHenshin_text_node(henshin_text_Node henshin_text_node) {
        this.henshin_text_node = henshin_text_node;
    }

}