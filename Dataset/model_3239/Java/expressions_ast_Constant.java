





import java.util.List;
import java.util.ArrayList;

public class expressions_ast_Constant extends Expression {

    private String value;



    public expressions_ast_Constant(
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