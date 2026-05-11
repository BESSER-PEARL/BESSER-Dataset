





import java.util.List;
import java.util.ArrayList;

public class feature_Feature  {

    private boolean isSelected;
    private int min;
    private String attribute;
    private String name;
    private int max;





    private List<feature_Feature> feature_features;


    public feature_Feature(
        boolean isSelected,        int min,        String attribute,        String name,        int max    ) {
        this.isSelected = isSelected;
        this.min = min;
        this.attribute = attribute;
        this.name = name;
        this.max = max;
        this.feature_features = new ArrayList<>();
    }

    public feature_Feature(
        boolean isSelected,        int min,        String attribute,        String name,        int max        ArrayList<feature_Feature> feature_features    ) {
        this.isSelected = isSelected;
        this.min = min;
        this.attribute = attribute;
        this.name = name;
        this.max = max;
        this.feature_features = feature_features;
    }

    public boolean getIsselected() {
        return isSelected;
    }

    public void setIsselected(boolean isSelected) {
        this.isSelected = isSelected;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public List<feature_Feature> getFeature_features() {
        return feature_features;
    }

    public void addFeature_feature(Feature_feature feature_feature) {
        this.feature_features.add(feature_feature);
    }

}