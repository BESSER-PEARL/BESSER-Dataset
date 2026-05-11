





import java.util.List;
import java.util.ArrayList;

public class sparrow_Sms extends Action {

    private String value;
    private String target;



    public sparrow_Sms(
        String value,        String target    ) {
        super(
        );
        this.value = value;
        this.target = target;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}