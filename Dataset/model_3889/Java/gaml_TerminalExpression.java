





import java.util.List;
import java.util.ArrayList;

public class gaml_TerminalExpression extends Expression {

    private String op;



    public gaml_TerminalExpression(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }


}