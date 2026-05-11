





import java.util.List;
import java.util.ArrayList;

public class carnot_Code  {

    private String value;
    private String name;
    private String code;





    private carnot_ActivityType carnot_activitytype;


    public carnot_Code(
        String value,        String name,        String code    ) {
        this.value = value;
        this.name = name;
        this.code = code;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }

}