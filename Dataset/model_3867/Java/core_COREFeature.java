





import java.util.List;
import java.util.ArrayList;

public class core_COREFeature extends COREModelElement {

    private String parentRelationship;





    private core_COREFeature core_corefeature;




    private core_COREFeature core_corefeature;




    private List<core_COREModel> core_coremodels;




    private List<core_COREReuse> core_corereuses;




    private List<core_COREFeature> core_corefeatures;




    private core_COREFeature core_corefeature;




    private core_COREModel core_coremodel;


    public core_COREFeature(
        String parentRelationship    ) {
        super(
        );
        this.parentRelationship = parentRelationship;
        this.core_coremodels = new ArrayList<>();
        this.core_corereuses = new ArrayList<>();
        this.core_corefeatures = new ArrayList<>();
    }

    public core_COREFeature(
        String parentRelationship        ArrayList<core_COREModel> core_coremodels,        ArrayList<core_COREReuse> core_corereuses,        ArrayList<core_COREFeature> core_corefeatures    ) {
        this.parentRelationship = parentRelationship;
        this.core_coremodels = core_coremodels;
        this.core_corereuses = core_corereuses;
        this.core_corefeatures = core_corefeatures;
    }

    public String getParentrelationship() {
        return parentRelationship;
    }

    public void setParentrelationship(String parentRelationship) {
        this.parentRelationship = parentRelationship;
    }

    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public List<core_COREModel> getCore_coremodels() {
        return core_coremodels;
    }

    public void addCore_coremodel(Core_coremodel core_coremodel) {
        this.core_coremodels.add(core_coremodel);
    }
    public List<core_COREReuse> getCore_corereuses() {
        return core_corereuses;
    }

    public void addCore_corereuse(Core_corereuse core_corereuse) {
        this.core_corereuses.add(core_corereuse);
    }
    public List<core_COREFeature> getCore_corefeatures() {
        return core_corefeatures;
    }

    public void addCore_corefeature(Core_corefeature core_corefeature) {
        this.core_corefeatures.add(core_corefeature);
    }
    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }

}