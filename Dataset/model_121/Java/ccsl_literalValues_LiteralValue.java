





import java.util.List;
import java.util.ArrayList;

public class ccsl_literalValues_LiteralValue extends Statement {

    private String value;



    public ccsl_literalValues_LiteralValue(
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