





import java.util.List;
import java.util.ArrayList;

public class petrinetmodel_EdgeToPlace extends Edge {






    private petrinetmodel_Transition petrinetmodel_transition;




    private petrinetmodel_Place petrinetmodel_place;


    public petrinetmodel_EdgeToPlace(
    ) {
        super(
        );
    }



    public petrinetmodel_Transition getPetrinetmodel_transition() {
        return petrinetmodel_transition;
    }

    public void setPetrinetmodel_transition(petrinetmodel_Transition petrinetmodel_transition) {
        this.petrinetmodel_transition = petrinetmodel_transition;
    }
    public petrinetmodel_Place getPetrinetmodel_place() {
        return petrinetmodel_place;
    }

    public void setPetrinetmodel_place(petrinetmodel_Place petrinetmodel_place) {
        this.petrinetmodel_place = petrinetmodel_place;
    }

}