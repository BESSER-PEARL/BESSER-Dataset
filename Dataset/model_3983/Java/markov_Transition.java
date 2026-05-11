





import java.util.List;
import java.util.ArrayList;

public class markov_Transition extends Entity {

    private float probability;





    private markov_State markov_state;




    private markov_State markov_state;




    private markov_MarkovChain markov_markovchain;


    public markov_Transition(
        float probability    ) {
        super(
        );
        this.probability = probability;
    }


    public float getProbability() {
        return probability;
    }

    public void setProbability(float probability) {
        this.probability = probability;
    }

    public markov_State getMarkov_state() {
        return markov_state;
    }

    public void setMarkov_state(markov_State markov_state) {
        this.markov_state = markov_state;
    }
    public markov_State getMarkov_state() {
        return markov_state;
    }

    public void setMarkov_state(markov_State markov_state) {
        this.markov_state = markov_state;
    }
    public markov_MarkovChain getMarkov_markovchain() {
        return markov_markovchain;
    }

    public void setMarkov_markovchain(markov_MarkovChain markov_markovchain) {
        this.markov_markovchain = markov_markovchain;
    }

}