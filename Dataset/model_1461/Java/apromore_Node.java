





import java.util.List;
import java.util.ArrayList;

public class apromore_Node  {

    private String name;
    private boolean configurable;
    private int ident;





    private apromore_Edge apromore_edge;




    private apromore_Net apromore_net;




    private apromore_Edge apromore_edge;


    public apromore_Node(
        String name,        boolean configurable,        int ident    ) {
        this.name = name;
        this.configurable = configurable;
        this.ident = ident;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getConfigurable() {
        return configurable;
    }

    public void setConfigurable(boolean configurable) {
        this.configurable = configurable;
    }
    public int getIdent() {
        return ident;
    }

    public void setIdent(int ident) {
        this.ident = ident;
    }

    public apromore_Edge getApromore_edge() {
        return apromore_edge;
    }

    public void setApromore_edge(apromore_Edge apromore_edge) {
        this.apromore_edge = apromore_edge;
    }
    public apromore_Net getApromore_net() {
        return apromore_net;
    }

    public void setApromore_net(apromore_Net apromore_net) {
        this.apromore_net = apromore_net;
    }
    public apromore_Edge getApromore_edge() {
        return apromore_edge;
    }

    public void setApromore_edge(apromore_Edge apromore_edge) {
        this.apromore_edge = apromore_edge;
    }

}