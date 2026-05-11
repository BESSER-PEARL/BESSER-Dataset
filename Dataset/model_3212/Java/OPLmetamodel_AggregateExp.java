





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_AggregateExp extends Expression {

    private String op;



    public OPLmetamodel_AggregateExp(
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