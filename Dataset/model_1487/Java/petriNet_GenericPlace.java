





import java.util.List;
import java.util.ArrayList;

public class petriNet_GenericPlace  {

    private int numberOfTokens;
    private String name;





    private petriNet_PetriNet petrinet_petrinet;


    public petriNet_GenericPlace(
        int numberOfTokens,        String name    ) {
        this.numberOfTokens = numberOfTokens;
        this.name = name;
    }


    public int getNumberoftokens() {
        return numberOfTokens;
    }

    public void setNumberoftokens(int numberOfTokens) {
        this.numberOfTokens = numberOfTokens;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petriNet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petriNet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}