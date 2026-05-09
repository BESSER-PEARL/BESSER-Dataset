





import java.util.List;
import java.util.ArrayList;

public class PN_Place  {

    private String name;





    private PN_Net pn_net;


    public PN_Place(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PN_Net getPn_net() {
        return pn_net;
    }

    public void setPn_net(PN_Net pn_net) {
        this.pn_net = pn_net;
    }

}