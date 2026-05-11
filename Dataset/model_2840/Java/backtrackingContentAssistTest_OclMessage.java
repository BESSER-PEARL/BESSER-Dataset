





import java.util.List;
import java.util.ArrayList;

public class backtrackingContentAssistTest_OclMessage extends Expression {

    private String op;
    private String messageName;



    public backtrackingContentAssistTest_OclMessage(
        String op,        String messageName    ) {
        super(
        );
        this.op = op;
        this.messageName = messageName;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getMessagename() {
        return messageName;
    }

    public void setMessagename(String messageName) {
        this.messageName = messageName;
    }


}