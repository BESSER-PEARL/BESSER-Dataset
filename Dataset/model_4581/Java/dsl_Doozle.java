





import java.util.List;
import java.util.ArrayList;

public class dsl_Doozle extends Action {

    private String on;
    private String value;
    private String target;



    public dsl_Doozle(
        String on,        String value,        String target    ) {
        super(
        );
        this.on = on;
        this.value = value;
        this.target = target;
    }


    public String getOn() {
        return on;
    }

    public void setOn(String on) {
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


}