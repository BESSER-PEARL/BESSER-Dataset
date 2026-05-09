





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Node {






    private petrinet_Token petrinet_token;




    private List<petrinet_Token> petrinet_tokens;


    public petrinet_Place(
    ) {
        super(
        );
        this.petrinet_tokens = new ArrayList<>();
    }

    public petrinet_Place(
        ArrayList<petrinet_Token> petrinet_tokens    ) {
        this.petrinet_tokens = petrinet_tokens;
    }


    public petrinet_Token getPetrinet_token() {
        return petrinet_token;
    }

    public void setPetrinet_token(petrinet_Token petrinet_token) {
        this.petrinet_token = petrinet_token;
    }
    public List<petrinet_Token> getPetrinet_tokens() {
        return petrinet_tokens;
    }

    public void addPetrinet_token(Petrinet_token petrinet_token) {
        this.petrinet_tokens.add(petrinet_token);
    }

}