





import java.util.List;
import java.util.ArrayList;

public class codemodel_expressions_LiteralExp extends Expression {

    private String value;



    public codemodel_expressions_LiteralExp(
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