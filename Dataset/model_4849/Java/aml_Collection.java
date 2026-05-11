





import java.util.List;
import java.util.ArrayList;

public class aml_Collection  {

    private String objectType;
    private String id;
    private String label;
    private String group;
    private String label1;



    public aml_Collection(
        String objectType,        String id,        String label,        String group,        String label1    ) {
        this.objectType = objectType;
        this.id = id;
        this.label = label;
        this.group = group;
        this.label1 = label1;
    }


    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getLabel1() {
        return label1;
    }

    public void setLabel1(String label1) {
        this.label1 = label1;
    }


}