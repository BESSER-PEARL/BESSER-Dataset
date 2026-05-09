





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Net  {






    private PetriNet_Place petrinet_place;




    private List<PetriNet_Place> petrinet_places;


    public PetriNet_Net(
    ) {
        this.petrinet_places = new ArrayList<>();
    }

    public PetriNet_Net(
        ArrayList<PetriNet_Place> petrinet_places    ) {
        this.petrinet_places = petrinet_places;
    }


    public PetriNet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(PetriNet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public List<PetriNet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}