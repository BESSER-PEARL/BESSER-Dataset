





import java.util.List;
import java.util.ArrayList;

public class alf_CollectOrIterateOperation extends SequenceExpansionExpression {

    private String op;



    public alf_CollectOrIterateOperation(
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