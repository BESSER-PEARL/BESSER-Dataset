





import java.util.List;
import java.util.ArrayList;

public class pn_Transition extends NetElement {






    private List<pn_Place> pn_places;




    private pn_Place pn_place;




    private List<pn_Place> pn_places;




    private pn_Place pn_place;


    public pn_Transition(
    ) {
        super(
        );
        this.pn_places = new ArrayList<>();
        this.pn_places = new ArrayList<>();
    }

    public pn_Transition(
        ArrayList<pn_Place> pn_places,        ArrayList<pn_Place> pn_places    ) {
        this.pn_places = pn_places;
        this.pn_places = pn_places;
    }


    public List<pn_Place> getPn_places() {
        return pn_places;
    }

    public void addPn_place(Pn_place pn_place) {
        this.pn_places.add(pn_place);
    }
    public pn_Place getPn_place() {
        return pn_place;
    }

    public void setPn_place(pn_Place pn_place) {
        this.pn_place = pn_place;
    }
    public List<pn_Place> getPn_places() {
        return pn_places;
    }

    public void addPn_place(Pn_place pn_place) {
        this.pn_places.add(pn_place);
    }
    public pn_Place getPn_place() {
        return pn_place;
    }

    public void setPn_place(pn_Place pn_place) {
        this.pn_place = pn_place;
    }

}