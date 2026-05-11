





import java.util.List;
import java.util.ArrayList;

public class BasicFMmetamodel_Feature  {

    private String name;
    private String id;
    private boolean selected;
    private boolean mandatory;





    private List<BasicFMmetamodel_Feature> basicfmmetamodel_features;




    private BasicFMmetamodel_FeatureModel basicfmmetamodel_featuremodel;




    private BasicFMmetamodel_Feature basicfmmetamodel_feature;




    private BasicFMmetamodel_FeatureModel basicfmmetamodel_featuremodel;


    public BasicFMmetamodel_Feature(
        String name,        String id,        boolean selected,        boolean mandatory    ) {
        this.name = name;
        this.id = id;
        this.selected = selected;
        this.mandatory = mandatory;
        this.basicfmmetamodel_features = new ArrayList<>();
    }

    public BasicFMmetamodel_Feature(
        String name,        String id,        boolean selected,        boolean mandatory        ArrayList<BasicFMmetamodel_Feature> basicfmmetamodel_features    ) {
        this.name = name;
        this.id = id;
        this.selected = selected;
        this.mandatory = mandatory;
        this.basicfmmetamodel_features = basicfmmetamodel_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }

    public List<BasicFMmetamodel_Feature> getBasicfmmetamodel_features() {
        return basicfmmetamodel_features;
    }

    public void addBasicfmmetamodel_feature(Basicfmmetamodel_feature basicfmmetamodel_feature) {
        this.basicfmmetamodel_features.add(basicfmmetamodel_feature);
    }
    public BasicFMmetamodel_FeatureModel getBasicfmmetamodel_featuremodel() {
        return basicfmmetamodel_featuremodel;
    }

    public void setBasicfmmetamodel_featuremodel(BasicFMmetamodel_FeatureModel basicfmmetamodel_featuremodel) {
        this.basicfmmetamodel_featuremodel = basicfmmetamodel_featuremodel;
    }
    public BasicFMmetamodel_Feature getBasicfmmetamodel_feature() {
        return basicfmmetamodel_feature;
    }

    public void setBasicfmmetamodel_feature(BasicFMmetamodel_Feature basicfmmetamodel_feature) {
        this.basicfmmetamodel_feature = basicfmmetamodel_feature;
    }
    public BasicFMmetamodel_FeatureModel getBasicfmmetamodel_featuremodel() {
        return basicfmmetamodel_featuremodel;
    }

    public void setBasicfmmetamodel_featuremodel(BasicFMmetamodel_FeatureModel basicfmmetamodel_featuremodel) {
        this.basicfmmetamodel_featuremodel = basicfmmetamodel_featuremodel;
    }

}