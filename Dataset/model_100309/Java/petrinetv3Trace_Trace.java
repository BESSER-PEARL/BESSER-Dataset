





import java.util.List;
import java.util.ArrayList;

public class petrinetv3Trace_Trace  {






    private List<petrinetv3_TracedPlace> petrinetv3_tracedplaces;


    public petrinetv3Trace_Trace(
    ) {
        this.petrinetv3_tracedplaces = new ArrayList<>();
    }

    public petrinetv3Trace_Trace(
        ArrayList<petrinetv3_TracedPlace> petrinetv3_tracedplaces    ) {
        this.petrinetv3_tracedplaces = petrinetv3_tracedplaces;
    }


    public List<petrinetv3_TracedPlace> getPetrinetv3_tracedplaces() {
        return petrinetv3_tracedplaces;
    }

    public void addPetrinetv3_tracedplace(Petrinetv3_tracedplace petrinetv3_tracedplace) {
        this.petrinetv3_tracedplaces.add(petrinetv3_tracedplace);
    }

}