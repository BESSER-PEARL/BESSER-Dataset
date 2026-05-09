





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition  {

    private String name;





    private List<petrinet_Place> petrinet_places;




    private petrinet_Net petrinet_net;




    private List<petrinet_Place> petrinet_places;


    public petrinet_Transition(
        String name    ) {
        this.name = name;
        this.petrinet_places = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
    }

    public petrinet_Transition(
        String name        ArrayList<petrinet_Place> petrinet_places,        ArrayList<petrinet_Place> petrinet_places    ) {
        this.name = name;
        this.petrinet_places = petrinet_places;
        this.petrinet_places = petrinet_places;
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
    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }
    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}