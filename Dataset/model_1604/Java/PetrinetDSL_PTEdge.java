





import java.util.List;
import java.util.ArrayList;

public class PetrinetDSL_PTEdge extends Edge {






    private PetrinetDSL_Place petrinetdsl_place;




    private PetrinetDSL_Transition petrinetdsl_transition;


    public PetrinetDSL_PTEdge(
    ) {
        super(
        );
    }



    public PetrinetDSL_Place getPetrinetdsl_place() {
        return petrinetdsl_place;
    }

    public void setPetrinetdsl_place(PetrinetDSL_Place petrinetdsl_place) {
        this.petrinetdsl_place = petrinetdsl_place;
    }
    public PetrinetDSL_Transition getPetrinetdsl_transition() {
        return petrinetdsl_transition;
    }

    public void setPetrinetdsl_transition(PetrinetDSL_Transition petrinetdsl_transition) {
        this.petrinetdsl_transition = petrinetdsl_transition;
    }

}