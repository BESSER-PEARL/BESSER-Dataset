





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition  {

    private int id;
    private String name;





    private List<petrinet_Place> petrinet_places;




    private petrinet_Place petrinet_place;


    public petrinet_Transition(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
        this.petrinet_places = new ArrayList<>();
    }

    public petrinet_Transition(
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
    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}