





import java.util.List;
import java.util.ArrayList;

public class SMTlib2extended_BitstringExpression extends ConstExpression {

    private String value;



    public SMTlib2extended_BitstringExpression(
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