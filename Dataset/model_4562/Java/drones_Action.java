





import java.util.List;
import java.util.ArrayList;

public class drones_Action extends NamedElement, TemporalContainmentProxy {

    private float range;
    private String value;
    private String key;
    private String operation;



    public drones_Action(
        float range,        String value,        String key,        String operation    ) {
        super(
        );
        this.range = range;
        this.value = value;
        this.key = key;
        this.operation = operation;
    }


    public float getRange() {
        return range;
    }

    public void setRange(float range) {
        this.range = range;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }


}