





import java.util.List;
import java.util.ArrayList;

public class dbl_WhileStatement extends CompositeStatement {






    private dbl_CodeBlock dbl_codeblock;




    private dbl_Expression dbl_expression;


    public dbl_WhileStatement(
    ) {
        super(
        );
    }



    public dbl_CodeBlock getDbl_codeblock() {
        return dbl_codeblock;
    }

    public void setDbl_codeblock(dbl_CodeBlock dbl_codeblock) {
        this.dbl_codeblock = dbl_codeblock;
    }
    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }

}