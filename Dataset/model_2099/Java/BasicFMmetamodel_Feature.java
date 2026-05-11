





import java.util.List;
import java.util.ArrayList;

public class BasicFMmetamodel_Feature  {

    private boolean selected;
    private String name;
    private boolean mandatory;
    private String id;





    private BasicFMmetamodel_Feature basicfmmetamodel_feature;




    private List<BasicFMmetamodel_Feature> basicfmmetamodel_features;




    private BasicFMmetamodel_FeatureModel basicfmmetamodel_featuremodel;


    public BasicFMmetamodel_Feature(
        boolean selected,        String name,        boolean mandatory,        String id    ) {
        this.selected = selected;
        this.name = name;
        this.mandatory = mandatory;
        this.id = id;
        this.basicfmmetamodel_features = new ArrayList<>();
    }

    public BasicFMmetamodel_Feature(
        boolean selected,        String name,        boolean mandatory,        String id        ArrayList<BasicFMmetamodel_Feature> basicfmmetamodel_features    ) {
        this.selected = selected;
        this.name = name;
        this.mandatory = mandatory;
        this.id = id;
        this.basicfmmetamodel_features = basicfmmetamodel_features;
    }

    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public BasicFMmetamodel_Feature getBasicfmmetamodel_feature() {
        return basicfmmetamodel_feature;
    }

    public void setBasicfmmetamodel_feature(BasicFMmetamodel_Feature basicfmmetamodel_feature) {
        this.basicfmmetamodel_feature = basicfmmetamodel_feature;
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

}