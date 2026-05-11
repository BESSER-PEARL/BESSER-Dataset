





import java.util.List;
import java.util.ArrayList;

public class Behaviour_TransitionFunction  {

    private String transitionFunction;





    private Behaviour_PostTransitionConnection behaviour_posttransitionconnection;




    private Behaviour_ConditionalTransition behaviour_conditionaltransition;




    private List<Behaviour_Token> behaviour_tokens;




    private Behaviour_StochasticTransition behaviour_stochastictransition;


    public Behaviour_TransitionFunction(
        String transitionFunction    ) {
        this.transitionFunction = transitionFunction;
        this.behaviour_tokens = new ArrayList<>();
    }

    public Behaviour_TransitionFunction(
        String transitionFunction        ArrayList<Behaviour_Token> behaviour_tokens    ) {
        this.transitionFunction = transitionFunction;
        this.behaviour_tokens = behaviour_tokens;
    }

    public String getTransitionfunction() {
        return transitionFunction;
    }

    public void setTransitionfunction(String transitionFunction) {
        this.transitionFunction = transitionFunction;
    }

    public Behaviour_PostTransitionConnection getBehaviour_posttransitionconnection() {
        return behaviour_posttransitionconnection;
    }

    public void setBehaviour_posttransitionconnection(Behaviour_PostTransitionConnection behaviour_posttransitionconnection) {
        this.behaviour_posttransitionconnection = behaviour_posttransitionconnection;
    }
    public Behaviour_ConditionalTransition getBehaviour_conditionaltransition() {
        return behaviour_conditionaltransition;
    }

    public void setBehaviour_conditionaltransition(Behaviour_ConditionalTransition behaviour_conditionaltransition) {
        this.behaviour_conditionaltransition = behaviour_conditionaltransition;
    }
    public List<Behaviour_Token> getBehaviour_tokens() {
        return behaviour_tokens;
    }

    public void addBehaviour_token(Behaviour_token behaviour_token) {
        this.behaviour_tokens.add(behaviour_token);
    }
    public Behaviour_StochasticTransition getBehaviour_stochastictransition() {
        return behaviour_stochastictransition;
    }

    public void setBehaviour_stochastictransition(Behaviour_StochasticTransition behaviour_stochastictransition) {
        this.behaviour_stochastictransition = behaviour_stochastictransition;
    }

}