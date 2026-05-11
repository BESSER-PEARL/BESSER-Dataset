





import java.util.List;
import java.util.ArrayList;

public class pascal_repetitive_arit_expression  {

    private String value;
    private String op;





    private pascal_arit_expression pascal_arit_expression;




    private pascal_repetitive_arit_expression pascal_repetitive_arit_expression;


    public pascal_repetitive_arit_expression(
        String value,        String op    ) {
        this.value = value;
        this.op = op;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public pascal_arit_expression getPascal_arit_expression() {
        return pascal_arit_expression;
    }

    public void setPascal_arit_expression(pascal_arit_expression pascal_arit_expression) {
        this.pascal_arit_expression = pascal_arit_expression;
    }
    public pascal_repetitive_arit_expression getPascal_repetitive_arit_expression() {
        return pascal_repetitive_arit_expression;
    }

    public void setPascal_repetitive_arit_expression(pascal_repetitive_arit_expression pascal_repetitive_arit_expression) {
        this.pascal_repetitive_arit_expression = pascal_repetitive_arit_expression;
    }

}