





import java.util.List;
import java.util.ArrayList;

public class MMInterModel_Attribute extends Element {

    private int lowerBound;
    private String model;
    private boolean isArray;
    private int arraySize;
    private String component;
    private String defaultValue;
    private String type;
    private int upperBound;





    private MMInterModel_Model mmintermodel_model;


    public MMInterModel_Attribute(
        int lowerBound,        String model,        boolean isArray,        int arraySize,        String component,        String defaultValue,        String type,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.model = model;
        this.isArray = isArray;
        this.arraySize = arraySize;
        this.component = component;
        this.defaultValue = defaultValue;
        this.type = type;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }
    public int getArraysize() {
        return arraySize;
    }

    public void setArraysize(int arraySize) {
        this.arraySize = arraySize;
    }
    public String getComponent() {
        return component;
    }

    public void setComponent(String component) {
        this.component = component;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public MMInterModel_Model getMmintermodel_model() {
        return mmintermodel_model;
    }

    public void setMmintermodel_model(MMInterModel_Model mmintermodel_model) {
        this.mmintermodel_model = mmintermodel_model;
    }

}