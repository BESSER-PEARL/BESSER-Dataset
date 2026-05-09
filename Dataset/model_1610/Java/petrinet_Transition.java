





import java.util.List;
import java.util.ArrayList;

public class petrinet_Transition extends NamedElement {






    private petrinet_Net petrinet_net;




    private petrinet_Net petrinet_net;




    private petrinet_Place petrinet_place;




    private petrinet_Place petrinet_place;




    private List<petrinet_Place> petrinet_places;




    private List<petrinet_Place> petrinet_places;


    public petrinet_Transition(
    ) {
        super(
        );
        this.petrinet_places = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
    }

    public petrinet_Transition(
        ArrayList<petrinet_Place> petrinet_places,        ArrayList<petrinet_Place> petrinet_places    ) {
        this.petrinet_places = petrinet_places;
        this.petrinet_places = petrinet_places;
    }


    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }
    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }
    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }
    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}