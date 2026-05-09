





import java.util.List;
import java.util.ArrayList;

public class ccsl_numberFunctions_CcslIntegerLiteral extends CcslNumberFunction {

    private String value;



    public ccsl_numberFunctions_CcslIntegerLiteral(
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