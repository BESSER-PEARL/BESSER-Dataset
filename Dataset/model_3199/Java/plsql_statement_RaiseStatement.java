





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_RaiseStatement extends Statement {

    private String exception;



    public plsql_statement_RaiseStatement(
        String exception    ) {
        super(
        );
        this.exception = exception;
    }


    public String getException() {
        return exception;
    }

    public void setException(String exception) {
        this.exception = exception;
    }


}