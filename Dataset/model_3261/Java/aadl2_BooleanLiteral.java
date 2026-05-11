





import java.util.List;
import java.util.ArrayList;

public class aadl2_BooleanLiteral extends PropertyValue {

    private String value;



    public aadl2_BooleanLiteral(
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