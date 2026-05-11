





import java.util.List;
import java.util.ArrayList;

public class dbl_WhileStatement extends LoopStatement {






    private dbl_Expression dbl_expression;




    private dbl_Statement dbl_statement;


    public dbl_WhileStatement(
    ) {
        super(
        );
    }



    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }
    public dbl_Statement getDbl_statement() {
        return dbl_statement;
    }

    public void setDbl_statement(dbl_Statement dbl_statement) {
        this.dbl_statement = dbl_statement;
    }

}