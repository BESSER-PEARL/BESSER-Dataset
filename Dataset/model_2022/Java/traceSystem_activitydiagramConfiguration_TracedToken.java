





import java.util.List;
import java.util.ArrayList;

public class traceSystem_activitydiagramConfiguration_TracedToken  {






    private List<Token_holder_State> token_holder_states;


    public traceSystem_activitydiagramConfiguration_TracedToken(
    ) {
        this.token_holder_states = new ArrayList<>();
    }

    public traceSystem_activitydiagramConfiguration_TracedToken(
        ArrayList<Token_holder_State> token_holder_states    ) {
        this.token_holder_states = token_holder_states;
    }


    public List<Token_holder_State> getToken_holder_states() {
        return token_holder_states;
    }

    public void addToken_holder_state(Token_holder_state token_holder_state) {
        this.token_holder_states.add(token_holder_state);
    }

}