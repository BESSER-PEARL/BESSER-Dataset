





import java.util.List;
import java.util.ArrayList;

public class alf_SelectOrRejectOperation extends SequenceExpansionExpression {

    private String op;



    public alf_SelectOrRejectOperation(
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