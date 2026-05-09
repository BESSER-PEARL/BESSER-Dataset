





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;
    private int initialTokens;





    private petrinet_Net petrinet_net;


    public petrinet_Place(
        String name,        int initialTokens    ) {
        this.name = name;
        this.initialTokens = initialTokens;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }

    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }

}