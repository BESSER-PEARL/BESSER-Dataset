





import java.util.List;
import java.util.ArrayList;

public class urml_requirement_FunctionalRequirement extends Requirement {






    private List<AbstractFeature> abstractfeatures;


    public urml_requirement_FunctionalRequirement(
    ) {
        super(
        );
        this.abstractfeatures = new ArrayList<>();
    }

    public urml_requirement_FunctionalRequirement(
        ArrayList<AbstractFeature> abstractfeatures    ) {
        this.abstractfeatures = abstractfeatures;
    }


    public List<AbstractFeature> getAbstractfeatures() {
        return abstractfeatures;
    }

    public void addAbstractfeature(Abstractfeature abstractfeature) {
        this.abstractfeatures.add(abstractfeature);
    }

}