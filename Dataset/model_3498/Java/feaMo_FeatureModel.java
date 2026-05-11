





import java.util.List;
import java.util.ArrayList;

public class feaMo_FeatureModel  {

    private String name;





    private feaMo_Model feamo_model;




    private feaMo_FeamoFeatureConfig feamo_feamofeatureconfig;


    public feaMo_FeatureModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public feaMo_Model getFeamo_model() {
        return feamo_model;
    }

    public void setFeamo_model(feaMo_Model feamo_model) {
        this.feamo_model = feamo_model;
    }
    public feaMo_FeamoFeatureConfig getFeamo_feamofeatureconfig() {
        return feamo_feamofeatureconfig;
    }

    public void setFeamo_feamofeatureconfig(feaMo_FeamoFeatureConfig feamo_feamofeatureconfig) {
        this.feamo_feamofeatureconfig = feamo_feamofeatureconfig;
    }

}