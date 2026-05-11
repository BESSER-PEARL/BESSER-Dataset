





import java.util.List;
import java.util.ArrayList;

public class fm_Attribute  {

    private String defaultValue;
    private boolean minimize;
    private String minRangeValue;
    private String objectiveFunctionAggregator;
    private String maxRangeValue;
    private boolean alert;
    private String type;
    private String name;
    private boolean qualityAttribute;
    private String weight;
    private String description;
    private String id;
    private String comment;
    private boolean resourceAttribute;



    public fm_Attribute(
        String defaultValue,        boolean minimize,        String minRangeValue,        String objectiveFunctionAggregator,        String maxRangeValue,        boolean alert,        String type,        String name,        boolean qualityAttribute,        String weight,        String description,        String id,        String comment,        boolean resourceAttribute    ) {
        this.defaultValue = defaultValue;
        this.minimize = minimize;
        this.minRangeValue = minRangeValue;
        this.objectiveFunctionAggregator = objectiveFunctionAggregator;
        this.maxRangeValue = maxRangeValue;
        this.alert = alert;
        this.type = type;
        this.name = name;
        this.qualityAttribute = qualityAttribute;
        this.weight = weight;
        this.description = description;
        this.id = id;
        this.comment = comment;
        this.resourceAttribute = resourceAttribute;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getMinimize() {
        return minimize;
    }

    public void setMinimize(boolean minimize) {
        this.minimize = minimize;
    }
    public String getMinrangevalue() {
        return minRangeValue;
    }

    public void setMinrangevalue(String minRangeValue) {
        this.minRangeValue = minRangeValue;
    }
    public String getObjectivefunctionaggregator() {
        return objectiveFunctionAggregator;
    }

    public void setObjectivefunctionaggregator(String objectiveFunctionAggregator) {
        this.objectiveFunctionAggregator = objectiveFunctionAggregator;
    }
    public String getMaxrangevalue() {
        return maxRangeValue;
    }

    public void setMaxrangevalue(String maxRangeValue) {
        this.maxRangeValue = maxRangeValue;
    }
    public boolean getAlert() {
        return alert;
    }

    public void setAlert(boolean alert) {
        this.alert = alert;
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
    public boolean getQualityattribute() {
        return qualityAttribute;
    }

    public void setQualityattribute(boolean qualityAttribute) {
        this.qualityAttribute = qualityAttribute;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getResourceattribute() {
        return resourceAttribute;
    }

    public void setResourceattribute(boolean resourceAttribute) {
        this.resourceAttribute = resourceAttribute;
    }


}