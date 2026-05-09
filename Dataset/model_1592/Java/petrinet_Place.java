





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;
    private int tokens;





    private petrinet_Net petrinet_net;


    public petrinet_Place(
        String name,        int tokens    ) {
        this.name = name;
        this.tokens = tokens;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }

    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }

}