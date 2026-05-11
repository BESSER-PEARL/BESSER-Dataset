





import java.util.List;
import java.util.ArrayList;

public class carnot_DataPathType extends IIdentifiableModelElement {

    private String direction;
    private String key;
    private String descriptor;
    private String dataPath;





    private carnot_DataType carnot_datatype;




    private carnot_DataType carnot_datatype;




    private carnot_ProcessDefinitionType carnot_processdefinitiontype;


    public carnot_DataPathType(
        String direction,        String key,        String descriptor,        String dataPath    ) {
        super(
        );
        this.direction = direction;
        this.key = key;
        this.descriptor = descriptor;
        this.dataPath = dataPath;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getDescriptor() {
        return descriptor;
    }

    public void setDescriptor(String descriptor) {
        this.descriptor = descriptor;
    }
    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
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
    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }

}