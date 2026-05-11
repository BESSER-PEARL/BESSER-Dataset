





import java.util.List;
import java.util.ArrayList;

public class carnot_DataPathType extends IIdentifiableModelElement {

    private String dataPath;
    private String direction;
    private String descriptor;
    private String key;





    private carnot_DataType carnot_datatype;




    private carnot_DataType carnot_datatype;


    public carnot_DataPathType(
        String dataPath,        String direction,        String descriptor,        String key    ) {
        super(
        );
        this.dataPath = dataPath;
        this.direction = direction;
        this.descriptor = descriptor;
        this.key = key;
    }


    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }
    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }

}