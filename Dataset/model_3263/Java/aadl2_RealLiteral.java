





import java.util.List;
import java.util.ArrayList;

public class aadl2_RealLiteral extends NumberValue {

    private String value;



    public aadl2_RealLiteral(
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