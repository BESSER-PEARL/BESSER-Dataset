





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_StringValue extends PrimitiveValue {

    private String value;



    public fuml_Kernel_StringValue(
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