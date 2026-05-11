





import java.util.List;
import java.util.ArrayList;

public class modelDsl_StringValue extends Value {

    private String value;



    public modelDsl_StringValue(
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