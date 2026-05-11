





import java.util.List;
import java.util.ArrayList;

public class sparrow_Doozle extends Action {

    private String value;
    private String target;
    private String on;



    public sparrow_Doozle(
        String value,        String target,        String on    ) {
        super(
        );
        this.value = value;
        this.target = target;
        this.on = on;
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
    public String getOn() {
        return on;
    }

    public void setOn(String on) {
        this.on = on;
    }


}