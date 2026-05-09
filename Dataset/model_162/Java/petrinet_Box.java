





import java.util.List;
import java.util.ArrayList;

public class petrinet_Box  {

    private int id;
    private String name;





    private List<petrinet_Place> petrinet_places;




    private petrinet_Transition petrinet_transition;


    public petrinet_Box(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
        this.petrinet_places = new ArrayList<>();
    }

    public petrinet_Box(
        int id,        String name        ArrayList<petrinet_Place> petrinet_places    ) {
        this.id = id;
        this.name = name;
        this.petrinet_places = petrinet_places;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}