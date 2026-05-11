





import java.util.List;
import java.util.ArrayList;

public class common_DoubleValue extends Modifiable {

    private float value;
    private String identifier;





    private common_DoubleValueList common_doublevaluelist;


    public common_DoubleValue(
        float value,        String identifier    ) {
        super(
        );
        this.value = value;
        this.identifier = identifier;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public common_DoubleValueList getCommon_doublevaluelist() {
        return common_doublevaluelist;
    }

    public void setCommon_doublevaluelist(common_DoubleValueList common_doublevaluelist) {
        this.common_doublevaluelist = common_doublevaluelist;
    }

}