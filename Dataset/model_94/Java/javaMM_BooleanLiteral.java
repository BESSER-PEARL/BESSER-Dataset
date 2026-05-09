





import java.util.List;
import java.util.ArrayList;

public class javaMM_BooleanLiteral extends Expression {

    private String value;



    public javaMM_BooleanLiteral(
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