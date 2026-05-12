





import java.util.List;
import java.util.ArrayList;

public class StringValue extends ValueType {

    private String value;



    public StringValue(
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