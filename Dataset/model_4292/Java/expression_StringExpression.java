





import java.util.List;
import java.util.ArrayList;

public class expression_StringExpression extends SubExpression2 {

    private String value;



    public expression_StringExpression(
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