





import java.util.List;
import java.util.ArrayList;

public class builderState_UserDataEntry  {

    private String key;
    private String value;





    private builderState_EObjectDescription builderstate_eobjectdescription;


    public builderState_UserDataEntry(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public builderState_EObjectDescription getBuilderstate_eobjectdescription() {
        return builderstate_eobjectdescription;
    }

    public void setBuilderstate_eobjectdescription(builderState_EObjectDescription builderstate_eobjectdescription) {
        this.builderstate_eobjectdescription = builderstate_eobjectdescription;
    }

}