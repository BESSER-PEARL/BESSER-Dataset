





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Element  {

    private String name;





    private PetriNet_PetriNetRoot petrinet_petrinetroot;


    public PetriNet_Element(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_PetriNetRoot getPetrinet_petrinetroot() {
        return petrinet_petrinetroot;
    }

    public void setPetrinet_petrinetroot(PetriNet_PetriNetRoot petrinet_petrinetroot) {
        this.petrinet_petrinetroot = petrinet_petrinetroot;
    }

}