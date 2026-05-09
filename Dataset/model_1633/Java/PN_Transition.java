





import java.util.List;
import java.util.ArrayList;

public class PN_Transition  {

    private String input;





    private List<PN_Place> pn_places;




    private List<PN_Place> pn_places;




    private PN_Place pn_place;




    private PN_Net pn_net;




    private PN_Place pn_place;


    public PN_Transition(
        String input    ) {
        this.input = input;
        this.pn_places = new ArrayList<>();
        this.pn_places = new ArrayList<>();
    }

    public PN_Transition(
        String input        ArrayList<PN_Place> pn_places,        ArrayList<PN_Place> pn_places    ) {
        this.input = input;
        this.pn_places = pn_places;
        this.pn_places = pn_places;
    }

    public String getInput() {
        return input;
    }

    public void setInput(String input) {
        this.input = input;
    }

    public List<PN_Place> getPn_places() {
        return pn_places;
    }

    public void addPn_place(Pn_place pn_place) {
        this.pn_places.add(pn_place);
    }
    public List<PN_Place> getPn_places() {
        return pn_places;
    }

    public void addPn_place(Pn_place pn_place) {
        this.pn_places.add(pn_place);
    }
    public PN_Place getPn_place() {
        return pn_place;
    }

    public void setPn_place(PN_Place pn_place) {
        this.pn_place = pn_place;
    }
    public PN_Net getPn_net() {
        return pn_net;
    }

    public void setPn_net(PN_Net pn_net) {
        this.pn_net = pn_net;
    }
    public PN_Place getPn_place() {
        return pn_place;
    }

    public void setPn_place(PN_Place pn_place) {
        this.pn_place = pn_place;
    }

}