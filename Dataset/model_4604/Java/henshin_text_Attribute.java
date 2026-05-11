





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Attribute  {

    private String actiontype;
    private String update;





    private henshin_text_Expression henshin_text_expression;




    private henshin_text_MultiRuleReuseNode henshin_text_multirulereusenode;




    private henshin_text_Node henshin_text_node;


    public henshin_text_Attribute(
        String actiontype,        String update    ) {
        this.actiontype = actiontype;
        this.update = update;
    }


    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }
    public String getUpdate() {
        return update;
    }

    public void setUpdate(String update) {
        this.update = update;
    }

    public henshin_text_Expression getHenshin_text_expression() {
        return henshin_text_expression;
    }

    public void setHenshin_text_expression(henshin_text_Expression henshin_text_expression) {
        this.henshin_text_expression = henshin_text_expression;
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