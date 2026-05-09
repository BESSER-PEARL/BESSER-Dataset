





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private int initialTokens;
    private String name;





    private petrinet_Net petrinet_net;




    private petrinet_Transition petrinet_transition;




    private petrinet_Transition petrinet_transition;




    private List<petrinet_Token> petrinet_tokens;


    public petrinet_Place(
        int initialTokens,        String name    ) {
        this.initialTokens = initialTokens;
        this.name = name;
        this.petrinet_tokens = new ArrayList<>();
    }

    public petrinet_Place(
        int initialTokens,        String name        ArrayList<petrinet_Token> petrinet_tokens    ) {
        this.initialTokens = initialTokens;
        this.name = name;
        this.petrinet_tokens = petrinet_tokens;
    }

    public int getInitialtokens() {
        return initialTokens;
    }

    public void setInitialtokens(int initialTokens) {
        this.initialTokens = initialTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public List<petrinet_Token> getPetrinet_tokens() {
        return petrinet_tokens;
    }

    public void addPetrinet_token(Petrinet_token petrinet_token) {
        this.petrinet_tokens.add(petrinet_token);
    }

}