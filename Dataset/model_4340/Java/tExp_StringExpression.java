





import java.util.List;
import java.util.ArrayList;

public class tExp_StringExpression extends PrologExpression {

    private String value;



    public tExp_StringExpression(
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