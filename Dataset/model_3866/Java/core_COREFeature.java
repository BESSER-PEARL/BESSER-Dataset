





import java.util.List;
import java.util.ArrayList;

public class core_COREFeature extends COREModelElement {

    private String parentRelationship;





    private core_COREFeatureModel core_corefeaturemodel;




    private core_COREInterface core_coreinterface;




    private List<core_COREFeature> core_corefeatures;




    private core_COREFeature core_corefeature;




    private core_COREFeatureModel core_corefeaturemodel;




    private core_CORERelativity core_corerelativity;




    private core_COREFeature core_corefeature;




    private List<core_CORERelativity> core_corerelativitys;




    private core_COREFeature core_corefeature;


    public core_COREFeature(
        String parentRelationship    ) {
        super(
        );
        this.parentRelationship = parentRelationship;
        this.core_corefeatures = new ArrayList<>();
        this.core_corerelativitys = new ArrayList<>();
    }

    public core_COREFeature(
        String parentRelationship        ArrayList<core_COREFeature> core_corefeatures,        ArrayList<core_CORERelativity> core_corerelativitys    ) {
        this.parentRelationship = parentRelationship;
        this.core_corefeatures = core_corefeatures;
        this.core_corerelativitys = core_corerelativitys;
    }

    public String getParentrelationship() {
        return parentRelationship;
    }

    public void setParentrelationship(String parentRelationship) {
        this.parentRelationship = parentRelationship;
    }

    public core_COREFeatureModel getCore_corefeaturemodel() {
        return core_corefeaturemodel;
    }

    public void setCore_corefeaturemodel(core_COREFeatureModel core_corefeaturemodel) {
        this.core_corefeaturemodel = core_corefeaturemodel;
    }
    public core_COREInterface getCore_coreinterface() {
        return core_coreinterface;
    }

    public void setCore_coreinterface(core_COREInterface core_coreinterface) {
        this.core_coreinterface = core_coreinterface;
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
    public core_COREFeatureModel getCore_corefeaturemodel() {
        return core_corefeaturemodel;
    }

    public void setCore_corefeaturemodel(core_COREFeatureModel core_corefeaturemodel) {
        this.core_corefeaturemodel = core_corefeaturemodel;
    }
    public core_CORERelativity getCore_corerelativity() {
        return core_corerelativity;
    }

    public void setCore_corerelativity(core_CORERelativity core_corerelativity) {
        this.core_corerelativity = core_corerelativity;
    }
    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }
    public List<core_CORERelativity> getCore_corerelativitys() {
        return core_corerelativitys;
    }

    public void addCore_corerelativity(Core_corerelativity core_corerelativity) {
        this.core_corerelativitys.add(core_corerelativity);
    }
    public core_COREFeature getCore_corefeature() {
        return core_corefeature;
    }

    public void setCore_corefeature(core_COREFeature core_corefeature) {
        this.core_corefeature = core_corefeature;
    }

}