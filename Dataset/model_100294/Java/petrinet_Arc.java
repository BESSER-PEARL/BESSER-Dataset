





import java.util.List;
import java.util.ArrayList;

public class petrinet_Arc  {

    private int tokensCount;
    private String kind;
    private boolean readOnly;





    private petrinet_Network petrinet_network;




    private petrinet_Network petrinet_network;


    public petrinet_Arc(
        int tokensCount,        String kind,        boolean readOnly    ) {
        this.tokensCount = tokensCount;
        this.kind = kind;
        this.readOnly = readOnly;
    }


    public int getTokenscount() {
        return tokensCount;
    }

    public void setTokenscount(int tokensCount) {
        this.tokensCount = tokensCount;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }

    public petrinet_Network getPetrinet_network() {
        return petrinet_network;
    }

    public void setPetrinet_network(petrinet_Network petrinet_network) {
        this.petrinet_network = petrinet_network;
    }
    public petrinet_Network getPetrinet_network() {
        return petrinet_network;
    }

    public void setPetrinet_network(petrinet_Network petrinet_network) {
        this.petrinet_network = petrinet_network;
    }

}