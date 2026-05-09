





import java.util.List;
import java.util.ArrayList;

public class Petrinet_Place  {

    private int tokens;
    private String name;





    private Petrinet_PetriNet petrinet_petrinet;


    public Petrinet_Place(
        int tokens,        String name    ) {
        this.tokens = tokens;
        this.name = name;
    }


    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(Petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}