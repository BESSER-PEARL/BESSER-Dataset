





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ConditionType  {

    private String group;
    private String mixed;
    private String type;



    public xpdl1_ConditionType(
        String group,        String mixed,        String type    ) {
        this.group = group;
        this.mixed = mixed;
        this.type = type;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}