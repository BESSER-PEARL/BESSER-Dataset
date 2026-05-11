





import java.util.List;
import java.util.ArrayList;

public class debugSeq_QueryValue extends Expression {

    private String message;





    private debugSeq_Expression debugseq_expression;


    public debugSeq_QueryValue(
        String message    ) {
        super(
        );
        this.message = message;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public debugSeq_Expression getDebugseq_expression() {
        return debugseq_expression;
    }

    public void setDebugseq_expression(debugSeq_Expression debugseq_expression) {
        this.debugseq_expression = debugseq_expression;
    }

}