





import java.util.List;
import java.util.ArrayList;

public class gpfl_Variable extends GExpression {

    private String value;



    public gpfl_Variable(
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