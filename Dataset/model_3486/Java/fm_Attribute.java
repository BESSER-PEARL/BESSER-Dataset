





import java.util.List;
import java.util.ArrayList;

public class fm_Attribute  {

    private boolean resourceAttribute;
    private String comment;
    private String description;
    private String type;
    private String name;
    private String weight;
    private boolean qualityAttribute;
    private String defaultValue;
    private String objectiveFunctionAggregator;
    private String minRangeValue;
    private String maxRangeValue;
    private boolean minimize;
    private String id;





    private fm_Feature fm_feature;




    private fm_Feature fm_feature;


    public fm_Attribute(
        boolean resourceAttribute,        String comment,        String description,        String type,        String name,        String weight,        boolean qualityAttribute,        String defaultValue,        String objectiveFunctionAggregator,        String minRangeValue,        String maxRangeValue,        boolean minimize,        String id    ) {
        this.resourceAttribute = resourceAttribute;
        this.comment = comment;
        this.description = description;
        this.type = type;
        this.name = name;
        this.weight = weight;
        this.qualityAttribute = qualityAttribute;
        this.defaultValue = defaultValue;
        this.objectiveFunctionAggregator = objectiveFunctionAggregator;
        this.minRangeValue = minRangeValue;
        this.maxRangeValue = maxRangeValue;
        this.minimize = minimize;
        this.id = id;
    }


    public boolean getResourceattribute() {
        return resourceAttribute;
    }

    public void setResourceattribute(boolean resourceAttribute) {
        this.resourceAttribute = resourceAttribute;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public boolean getQualityattribute() {
        return qualityAttribute;
    }

    public void setQualityattribute(boolean qualityAttribute) {
        this.qualityAttribute = qualityAttribute;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getObjectivefunctionaggregator() {
        return objectiveFunctionAggregator;
    }

    public void setObjectivefunctionaggregator(String objectiveFunctionAggregator) {
        this.objectiveFunctionAggregator = objectiveFunctionAggregator;
    }
    public String getMinrangevalue() {
        return minRangeValue;
    }

    public void setMinrangevalue(String minRangeValue) {
        this.minRangeValue = minRangeValue;
    }
    public String getMaxrangevalue() {
        return maxRangeValue;
    }

    public void setMaxrangevalue(String maxRangeValue) {
        this.maxRangeValue = maxRangeValue;
    }
    public boolean getMinimize() {
        return minimize;
    }

    public void setMinimize(boolean minimize) {
        this.minimize = minimize;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }

}