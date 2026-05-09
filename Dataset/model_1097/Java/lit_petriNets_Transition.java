





import java.util.List;
import java.util.ArrayList;

public class lit_petriNets_Transition  {

    private String name;





    private List<lit_petriNets_Place> lit_petrinets_places;




    private lit_petriNets_Place lit_petrinets_place;




    private List<lit_petriNets_Place> lit_petrinets_places;




    private lit_petriNets_Place lit_petrinets_place;


    public lit_petriNets_Transition(
        String name    ) {
        this.name = name;
        this.lit_petrinets_places = new ArrayList<>();
        this.lit_petrinets_places = new ArrayList<>();
    }

    public lit_petriNets_Transition(
        String name        ArrayList<lit_petriNets_Place> lit_petrinets_places,        ArrayList<lit_petriNets_Place> lit_petrinets_places    ) {
        this.name = name;
        this.lit_petrinets_places = lit_petrinets_places;
        this.lit_petrinets_places = lit_petrinets_places;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<lit_petriNets_Place> getLit_petrinets_places() {
        return lit_petrinets_places;
    }

    public void addLit_petrinets_place(Lit_petrinets_place lit_petrinets_place) {
        this.lit_petrinets_places.add(lit_petrinets_place);
    }
    public lit_petriNets_Place getLit_petrinets_place() {
        return lit_petrinets_place;
    }

    public void setLit_petrinets_place(lit_petriNets_Place lit_petrinets_place) {
        this.lit_petrinets_place = lit_petrinets_place;
    }
    public List<lit_petriNets_Place> getLit_petrinets_places() {
        return lit_petrinets_places;
    }

    public void addLit_petrinets_place(Lit_petrinets_place lit_petrinets_place) {
        this.lit_petrinets_places.add(lit_petrinets_place);
    }
    public lit_petriNets_Place getLit_petrinets_place() {
        return lit_petrinets_place;
    }

    public void setLit_petrinets_place(lit_petriNets_Place lit_petrinets_place) {
        this.lit_petrinets_place = lit_petrinets_place;
    }

}