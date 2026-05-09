





import java.util.List;
import java.util.ArrayList;

public class Petrinet_Transition  {

    private String name;





    private Petrinet_PetriNet petrinet_petrinet;




    private Petrinet_Place petrinet_place;




    private List<Petrinet_Place> petrinet_places;


    public Petrinet_Transition(
        String name    ) {
        this.name = name;
        this.petrinet_places = new ArrayList<>();
    }

    public Petrinet_Transition(
        String name        ArrayList<Petrinet_Place> petrinet_places    ) {
        this.name = name;
        this.petrinet_places = petrinet_places;
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
    public Petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(Petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public List<Petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}