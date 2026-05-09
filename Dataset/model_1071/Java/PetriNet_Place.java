





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place  {

    private int tokens;





    private PetriNet_PetriNet petrinet_petrinet;


    public PetriNet_Place(
        int tokens    ) {
        this.tokens = tokens;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }

    public PetriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(PetriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}