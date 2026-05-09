





import java.util.List;
import java.util.ArrayList;

public class petri_Place  {

    private int token;





    private petri_PetriNet petri_petrinet;


    public petri_Place(
        int token    ) {
        this.token = token;
    }


    public int getToken() {
        return token;
    }

    public void setToken(int token) {
        this.token = token;
    }

    public petri_PetriNet getPetri_petrinet() {
        return petri_petrinet;
    }

    public void setPetri_petrinet(petri_PetriNet petri_petrinet) {
        this.petri_petrinet = petri_petrinet;
    }

}