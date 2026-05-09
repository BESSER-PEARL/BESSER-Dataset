





import java.util.List;
import java.util.ArrayList;

public class petrinet2_Transition  {

    private String name;





    private List<petrinet2_Place> petrinet2_places;




    private List<petrinet2_Place> petrinet2_places;




    private petrinet2_Net petrinet2_net;


    public petrinet2_Transition(
        String name    ) {
        this.name = name;
        this.petrinet2_places = new ArrayList<>();
        this.petrinet2_places = new ArrayList<>();
    }

    public petrinet2_Transition(
        String name        ArrayList<petrinet2_Place> petrinet2_places,        ArrayList<petrinet2_Place> petrinet2_places    ) {
        this.name = name;
        this.petrinet2_places = petrinet2_places;
        this.petrinet2_places = petrinet2_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet2_Place> getPetrinet2_places() {
        return petrinet2_places;
    }

    public void addPetrinet2_place(Petrinet2_place petrinet2_place) {
        this.petrinet2_places.add(petrinet2_place);
    }
    public List<petrinet2_Place> getPetrinet2_places() {
        return petrinet2_places;
    }

    public void addPetrinet2_place(Petrinet2_place petrinet2_place) {
        this.petrinet2_places.add(petrinet2_place);
    }
    public petrinet2_Net getPetrinet2_net() {
        return petrinet2_net;
    }

    public void setPetrinet2_net(petrinet2_Net petrinet2_net) {
        this.petrinet2_net = petrinet2_net;
    }

}