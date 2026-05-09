





import java.util.List;
import java.util.ArrayList;

public class petri_EdgeToPlace extends Edge {






    private petri_Transition petri_transition;




    private petri_Place petri_place;


    public petri_EdgeToPlace(
    ) {
        super(
        );
    }



    public petri_Transition getPetri_transition() {
        return petri_transition;
    }

    public void setPetri_transition(petri_Transition petri_transition) {
        this.petri_transition = petri_transition;
    }
    public petri_Place getPetri_place() {
        return petri_place;
    }

    public void setPetri_place(petri_Place petri_place) {
        this.petri_place = petri_place;
    }

}