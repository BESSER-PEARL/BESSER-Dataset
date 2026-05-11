





import java.util.List;
import java.util.ArrayList;

public class sparrow_Transform extends Action {

    private String on;
    private String value;



    public sparrow_Transform(
        String on,        String value    ) {
        super(
        );
        this.on = on;
        this.value = value;
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


}