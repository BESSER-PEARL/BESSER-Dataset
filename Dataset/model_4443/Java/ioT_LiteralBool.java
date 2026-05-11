





import java.util.List;
import java.util.ArrayList;

public class ioT_LiteralBool extends Condition {

    private String value;



    public ioT_LiteralBool(
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