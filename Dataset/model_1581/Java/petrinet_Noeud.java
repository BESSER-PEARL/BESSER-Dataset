





import java.util.List;
import java.util.ArrayList;

public class petrinet_Noeud  {

    private String name;





    private petrinet_PetriNet petrinet_petrinet;


    public petrinet_Noeud(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_PetriNet getPetrinet_petrinet() {
        return petrinet_petrinet;
    }

    public void setPetrinet_petrinet(petrinet_PetriNet petrinet_petrinet) {
        this.petrinet_petrinet = petrinet_petrinet;
    }

}