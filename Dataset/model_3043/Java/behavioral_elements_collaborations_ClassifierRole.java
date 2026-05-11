





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_collaborations_ClassifierRole extends Classifier {






    private List<ModelElement> modelelements;


    public behavioral_elements_collaborations_ClassifierRole(
    ) {
        super(
        );
        this.modelelements = new ArrayList<>();
    }

    public behavioral_elements_collaborations_ClassifierRole(
        ArrayList<ModelElement> modelelements    ) {
        this.modelelements = modelelements;
    }


    public List<ModelElement> getModelelements() {
        return modelelements;
    }

    public void addModelelement(Modelelement modelelement) {
        this.modelelements.add(modelelement);
    }

}