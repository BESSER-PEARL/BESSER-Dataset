





import java.util.List;
import java.util.ArrayList;

public class urml_requirement_NonFunctionalRequirement extends Requirement {






    private List<AbstractFeature> abstractfeatures;


    public urml_requirement_NonFunctionalRequirement(
    ) {
        super(
        );
        this.abstractfeatures = new ArrayList<>();
    }

    public urml_requirement_NonFunctionalRequirement(
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