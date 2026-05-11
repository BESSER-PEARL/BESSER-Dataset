





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_BinaryOperator extends AbstractBinaryOperator {

    private String op;



    public OPLmetamodel_BinaryOperator(
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