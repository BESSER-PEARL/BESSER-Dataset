





import java.util.List;
import java.util.ArrayList;

public class core_COREReuse  {






    private List<core_COREFeature> core_corefeatures;




    private core_COREModel core_coremodel;




    private List<core_CORECompositionSpecification> core_corecompositionspecifications;




    private core_COREConcern core_coreconcern;


    public core_COREReuse(
    ) {
        this.core_corefeatures = new ArrayList<>();
        this.core_corecompositionspecifications = new ArrayList<>();
    }

    public core_COREReuse(
        ArrayList<core_COREFeature> core_corefeatures,        ArrayList<core_CORECompositionSpecification> core_corecompositionspecifications    ) {
        this.core_corefeatures = core_corefeatures;
        this.core_corecompositionspecifications = core_corecompositionspecifications;
    }


    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }
    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }
    public List<core_CORECompositionSpecification> getCore_corecompositionspecifications() {
        return core_corecompositionspecifications;
    }

    public void addCore_corecompositionspecification(Core_corecompositionspecification core_corecompositionspecification) {
        this.core_corecompositionspecifications.add(core_corecompositionspecification);
    }
    public core_COREConcern getCore_coreconcern() {
        return core_coreconcern;
    }

    public void setCore_coreconcern(core_COREConcern core_coreconcern) {
        this.core_coreconcern = core_coreconcern;
    }

}