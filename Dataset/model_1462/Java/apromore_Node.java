





import java.util.List;
import java.util.ArrayList;

public class apromore_Node  {

    private String name;
    private int ident;
    private boolean configurable;





    private apromore_Net apromore_net;


    public apromore_Node(
        String name,        int ident,        boolean configurable    ) {
        this.name = name;
        this.ident = ident;
        this.configurable = configurable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIdent() {
        return ident;
    }

    public void setIdent(int ident) {
        this.ident = ident;
    }
    public boolean getConfigurable() {
        return configurable;
    }

    public void setConfigurable(boolean configurable) {
        this.configurable = configurable;
    }

    public apromore_Net getApromore_net() {
        return apromore_net;
    }

    public void setApromore_net(apromore_Net apromore_net) {
        this.apromore_net = apromore_net;
    }

}