





import java.util.List;
import java.util.ArrayList;

public class markov_State extends Entity {

    private String type;
    private String traces;





    private markov_MarkovChain markov_markovchain;


    public markov_State(
        String type,        String traces    ) {
        super(
        );
        this.type = type;
        this.traces = traces;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTraces() {
        return traces;
    }

    public void setTraces(String traces) {
        this.traces = traces;
    }

    public markov_MarkovChain getMarkov_markovchain() {
        return markov_markovchain;
    }

    public void setMarkov_markovchain(markov_MarkovChain markov_markovchain) {
        this.markov_markovchain = markov_markovchain;
    }

}