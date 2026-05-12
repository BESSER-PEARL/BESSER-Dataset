





import java.util.List;
import java.util.ArrayList;

public class plSql_FunctionInvokerRightsClause extends FunctionClause {

    private String right;



    public plSql_FunctionInvokerRightsClause(
        String right    ) {
        super(
        );
        this.right = right;
    }


    public String getRight() {
        return right;
    }

    public void setRight(String right) {
        this.right = right;
    }


}