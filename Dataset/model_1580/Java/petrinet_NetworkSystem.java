





import java.util.List;
import java.util.ArrayList;

public class petrinet_NetworkSystem  {






    private List<petrinet_PetriNet> petrinet_petrinets;


    public petrinet_NetworkSystem(
    ) {
        this.petrinet_petrinets = new ArrayList<>();
    }

    public petrinet_NetworkSystem(
        ArrayList<petrinet_PetriNet> petrinet_petrinets    ) {
        this.petrinet_petrinets = petrinet_petrinets;
    }


    public List<petrinet_PetriNet> getPetrinet_petrinets() {
        return petrinet_petrinets;
    }

    public void addPetrinet_petrinet(Petrinet_petrinet petrinet_petrinet) {
        this.petrinet_petrinets.add(petrinet_petrinet);
    }

}