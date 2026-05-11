





import java.util.List;
import java.util.ArrayList;

public class optGrammar_BooleanLiteral extends Literal {

    private String value;



    public optGrammar_BooleanLiteral(
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