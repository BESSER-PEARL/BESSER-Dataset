





import java.util.List;
import java.util.ArrayList;

public class sadl_UnaryOpExpression extends Expression {

    private String op;



    public sadl_UnaryOpExpression(
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