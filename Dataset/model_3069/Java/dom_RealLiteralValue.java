





import java.util.List;
import java.util.ArrayList;

public class dom_RealLiteralValue extends LiteralValue {

    private String value;



    public dom_RealLiteralValue(
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