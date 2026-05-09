





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place  {

    private String name;
    private int initialTokens;





    private List<petrinet_Token> petrinet_tokens;




    private petrinet_Transition petrinet_transition;




    private petrinet_Transition petrinet_transition;


    public petrinet_Place(
        String name,        int initialTokens    ) {
        this.name = name;
        this.initialTokens = initialTokens;
        this.petrinet_tokens = new ArrayList<>();
    }

    public petrinet_Place(
        String name,        int initialTokens        ArrayList<petrinet_Token> petrinet_tokens    ) {
        this.name = name;
        this.initialTokens = initialTokens;
        this.petrinet_tokens = petrinet_tokens;
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

    public List<petrinet_Token> getPetrinet_tokens() {
        return petrinet_tokens;
    }

    public void addPetrinet_token(Petrinet_token petrinet_token) {
        this.petrinet_tokens.add(petrinet_token);
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

}