





import java.util.List;
import java.util.ArrayList;

public class tExp_NumberExpression extends PrologExpression {

    private String value;



    public tExp_NumberExpression(
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