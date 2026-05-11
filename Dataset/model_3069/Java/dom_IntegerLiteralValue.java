





import java.util.List;
import java.util.ArrayList;

public class dom_IntegerLiteralValue extends LiteralValue {

    private String value;



    public dom_IntegerLiteralValue(
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