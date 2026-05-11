





import java.util.List;
import java.util.ArrayList;

public class vql_StringValue extends LiteralValueReference {

    private String value;



    public vql_StringValue(
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