





import java.util.List;
import java.util.ArrayList;

public class myDsl_StringType extends BasicType {

    private String value;



    public myDsl_StringType(
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