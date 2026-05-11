





import java.util.List;
import java.util.ArrayList;

public class umlTrace_IntermediateActivities_TracedToken  {






    private List<Token_holder_Value> token_holder_values;


    public umlTrace_IntermediateActivities_TracedToken(
    ) {
        this.token_holder_values = new ArrayList<>();
    }

    public umlTrace_IntermediateActivities_TracedToken(
        ArrayList<Token_holder_Value> token_holder_values    ) {
        this.token_holder_values = token_holder_values;
    }


    public List<Token_holder_Value> getToken_holder_values() {
        return token_holder_values;
    }

    public void addToken_holder_value(Token_holder_value token_holder_value) {
        this.token_holder_values.add(token_holder_value);
    }

}