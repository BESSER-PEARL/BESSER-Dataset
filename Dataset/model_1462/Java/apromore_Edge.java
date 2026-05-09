





import java.util.List;
import java.util.ArrayList;

public class apromore_Edge  {

    private boolean default;
    private String condition;
    private int ident;





    private apromore_Node apromore_node;




    private apromore_Net apromore_net;




    private apromore_Node apromore_node;


    public apromore_Edge(
        boolean default,        String condition,        int ident    ) {
        this.default = default;
        this.condition = condition;
        this.ident = ident;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }
    public int getIdent() {
        return ident;
    }

    public void setIdent(int ident) {
        this.ident = ident;
    }

    public apromore_Node getApromore_node() {
        return apromore_node;
    }

    public void setApromore_node(apromore_Node apromore_node) {
        this.apromore_node = apromore_node;
    }
    public apromore_Net getApromore_net() {
        return apromore_net;
    }

    public void setApromore_net(apromore_Net apromore_net) {
        this.apromore_net = apromore_net;
    }
    public apromore_Node getApromore_node() {
        return apromore_node;
    }

    public void setApromore_node(apromore_Node apromore_node) {
        this.apromore_node = apromore_node;
    }

}