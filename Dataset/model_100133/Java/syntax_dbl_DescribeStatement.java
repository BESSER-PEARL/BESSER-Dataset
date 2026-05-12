





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_DescribeStatement extends BindingStatement {

    private String statementName;



    public syntax_dbl_DescribeStatement(
        String statementName    ) {
        super(
        );
        this.statementName = statementName;
    }


    public String getStatementname() {
        return statementName;
    }

    public void setStatementname(String statementName) {
        this.statementName = statementName;
    }


}