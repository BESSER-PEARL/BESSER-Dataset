





import java.util.List;
import java.util.ArrayList;

public class dsl_Transform extends Action {

    private String value;
    private String on;



    public dsl_Transform(
        String value,        String on    ) {
        super(
        );
        this.value = value;
        this.on = on;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getOn() {
        return on;
    }

    public void setOn(String on) {
        this.on = on;
    }


}