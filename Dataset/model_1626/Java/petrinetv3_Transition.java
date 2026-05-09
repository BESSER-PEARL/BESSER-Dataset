





import java.util.List;
import java.util.ArrayList;

public class petrinetv3_Transition  {

    private int tmax;
    private int clock;
    private int tmin;
    private String name;





    private List<petrinetv3_Place> petrinetv3_places;




    private List<petrinetv3_Place> petrinetv3_places;




    private petrinetv3_Net petrinetv3_net;




    private petrinetv3_Net petrinetv3_net;


    public petrinetv3_Transition(
        int tmax,        int clock,        int tmin,        String name    ) {
        this.tmax = tmax;
        this.clock = clock;
        this.tmin = tmin;
        this.name = name;
        this.petrinetv3_places = new ArrayList<>();
        this.petrinetv3_places = new ArrayList<>();
    }

    public petrinetv3_Transition(
        int tmax,        int clock,        int tmin,        String name        ArrayList<petrinetv3_Place> petrinetv3_places,        ArrayList<petrinetv3_Place> petrinetv3_places    ) {
        this.tmax = tmax;
        this.clock = clock;
        this.tmin = tmin;
        this.name = name;
        this.petrinetv3_places = petrinetv3_places;
        this.petrinetv3_places = petrinetv3_places;
    }

    public int getTmax() {
        return tmax;
    }

    public void setTmax(int tmax) {
        this.tmax = tmax;
    }
    public int getClock() {
        return clock;
    }

    public void setClock(int clock) {
        this.clock = clock;
    }
    public int getTmin() {
        return tmin;
    }

    public void setTmin(int tmin) {
        this.tmin = tmin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinetv3_Place> getPetrinetv3_places() {
        return petrinetv3_places;
    }

    public void addPetrinetv3_place(Petrinetv3_place petrinetv3_place) {
        this.petrinetv3_places.add(petrinetv3_place);
    }
    public List<petrinetv3_Place> getPetrinetv3_places() {
        return petrinetv3_places;
    }

    public void addPetrinetv3_place(Petrinetv3_place petrinetv3_place) {
        this.petrinetv3_places.add(petrinetv3_place);
    }
    public petrinetv3_Net getPetrinetv3_net() {
        return petrinetv3_net;
    }

    public void setPetrinetv3_net(petrinetv3_Net petrinetv3_net) {
        this.petrinetv3_net = petrinetv3_net;
    }
    public petrinetv3_Net getPetrinetv3_net() {
        return petrinetv3_net;
    }

    public void setPetrinetv3_net(petrinetv3_Net petrinetv3_net) {
        this.petrinetv3_net = petrinetv3_net;
    }

}