





import java.util.List;
import java.util.ArrayList;

public class dsl_Number_Object extends Element {

    private String value;



    public dsl_Number_Object(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}