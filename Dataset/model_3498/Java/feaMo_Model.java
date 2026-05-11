





import java.util.List;
import java.util.ArrayList;

public class feaMo_Model  {






    private List<feaMo_FeamoFeatureConfig> feamo_feamofeatureconfigs;


    public feaMo_Model(
    ) {
        this.feamo_feamofeatureconfigs = new ArrayList<>();
    }

    public feaMo_Model(
        ArrayList<feaMo_FeamoFeatureConfig> feamo_feamofeatureconfigs    ) {
        this.feamo_feamofeatureconfigs = feamo_feamofeatureconfigs;
    }


    public List<feaMo_FeamoFeatureConfig> getFeamo_feamofeatureconfigs() {
        return feamo_feamofeatureconfigs;
    }

    public void addFeamo_feamofeatureconfig(Feamo_feamofeatureconfig feamo_feamofeatureconfig) {
        this.feamo_feamofeatureconfigs.add(feamo_feamofeatureconfig);
    }

}