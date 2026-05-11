





import java.util.List;
import java.util.ArrayList;

public class core_COREModel extends CORENamedElement {






    private core_COREFeature core_corefeature;




    private core_COREConcern core_coreconcern;




    private List<core_COREModelElement> core_coremodelelements;




    private core_CORECompositionSpecification core_corecompositionspecification;




    private List<core_COREFeature> core_corefeatures;


    public core_COREModel(
    ) {
        super(
        );
        this.core_coremodelelements = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREModel(
        ArrayList<core_COREModelElement> core_coremodelelements,        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.core_coremodelelements = core_coremodelelements;
        this.core_corefeatures = core_corefeatures;
    }


    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public core_COREConcern getCore_coreconcern() {
        return core_coreconcern;
    }

    public void setCore_coreconcern(core_COREConcern core_coreconcern) {
        this.core_coreconcern = core_coreconcern;
    }
    public List<core_COREModelElement> getCore_coremodelelements() {
        return core_coremodelelements;
    }

    public void addCore_coremodelelement(Core_coremodelelement core_coremodelelement) {
        this.core_coremodelelements.add(core_coremodelelement);
    }
    public core_CORECompositionSpecification getCore_corecompositionspecification() {
        return core_corecompositionspecification;
    }

    public void setCore_corecompositionspecification(core_CORECompositionSpecification core_corecompositionspecification) {
        this.core_corecompositionspecification = core_corecompositionspecification;
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }

}