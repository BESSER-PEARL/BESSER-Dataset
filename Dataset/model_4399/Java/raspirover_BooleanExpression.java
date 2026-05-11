





import java.util.List;
import java.util.ArrayList;

public class raspirover_BooleanExpression extends RoverExpression {

    private String op;



    public raspirover_BooleanExpression(
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