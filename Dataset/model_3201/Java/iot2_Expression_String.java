





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression_String extends Expression {

    private String value;



    public iot2_Expression_String(
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