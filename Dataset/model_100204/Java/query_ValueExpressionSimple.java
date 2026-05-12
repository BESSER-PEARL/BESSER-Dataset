





import java.util.List;
import java.util.ArrayList;

public class query_ValueExpressionSimple extends ValueExpressionAtomic {

    private String value;



    public query_ValueExpressionSimple(
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