





import java.util.List;
import java.util.ArrayList;

public class sql_UnipivotInClause extends UnpivotInClause {

    private String op;



    public sql_UnipivotInClause(
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