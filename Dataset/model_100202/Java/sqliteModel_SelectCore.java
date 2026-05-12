





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectCore extends SelectCoreExpression {

    private String op;



    public sqliteModel_SelectCore(
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