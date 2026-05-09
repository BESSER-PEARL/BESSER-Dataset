





import java.util.List;
import java.util.ArrayList;

public class petriNetz_Arc  {

    private int weight;





    private petriNetz_Petrinet petrinetz_petrinet;


    public petriNetz_Arc(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public petriNetz_Petrinet getPetrinetz_petrinet() {
        return petrinetz_petrinet;
    }

    public void setPetrinetz_petrinet(petriNetz_Petrinet petrinetz_petrinet) {
        this.petrinetz_petrinet = petrinetz_petrinet;
    }

}