





import java.util.List;
import java.util.ArrayList;

public class urml_requirement_FunctionalRequirement extends Requirement {






    private List<FunctionalRequirement> functionalrequirements;




    private FunctionalRequirement functionalrequirement;




    private List<AbstractFeature> abstractfeatures;


    public urml_requirement_FunctionalRequirement(
    ) {
        super(
        );
        this.functionalrequirements = new ArrayList<>();
        this.abstractfeatures = new ArrayList<>();
    }

    public urml_requirement_FunctionalRequirement(
        ArrayList<FunctionalRequirement> functionalrequirements,        ArrayList<AbstractFeature> abstractfeatures    ) {
        this.functionalrequirements = functionalrequirements;
        this.abstractfeatures = abstractfeatures;
    }


    public List<FunctionalRequirement> getFunctionalrequirements() {
        return functionalrequirements;
    }

    public void addFunctionalrequirement(Functionalrequirement functionalrequirement) {
        this.functionalrequirements.add(functionalrequirement);
    }
    public FunctionalRequirement getFunctionalrequirement() {
        return functionalrequirement;
    }

    public void setFunctionalrequirement(FunctionalRequirement functionalrequirement) {
        this.functionalrequirement = functionalrequirement;
    }
    public List<AbstractFeature> getAbstractfeatures() {
        return abstractfeatures;
    }

    public void addAbstractfeature(Abstractfeature abstractfeature) {
        this.abstractfeatures.add(abstractfeature);
    }

}