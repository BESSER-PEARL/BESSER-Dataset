





import java.util.List;
import java.util.ArrayList;

public class simplejava_StringExpression extends ConstantExpression {

    private String value;



    public simplejava_StringExpression(
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