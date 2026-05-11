





import java.util.List;
import java.util.ArrayList;

public class drones_Parameter extends TemporalContainmentProxy {

    private String value;
    private String key;





    private drones_FieldObject drones_fieldobject;


    public drones_Parameter(
        String value,        String key    ) {
        super(
        );
        this.value = value;
        this.key = key;
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

    public drones_FieldObject getDrones_fieldobject() {
        return drones_fieldobject;
    }

    public void setDrones_fieldobject(drones_FieldObject drones_fieldobject) {
        this.drones_fieldobject = drones_fieldobject;
    }

}