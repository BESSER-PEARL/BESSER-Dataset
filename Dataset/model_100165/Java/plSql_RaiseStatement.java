





import java.util.List;
import java.util.ArrayList;

public class plSql_RaiseStatement extends Statement {

    private String exceptionName;



    public plSql_RaiseStatement(
        String exceptionName    ) {
        super(
        );
        this.exceptionName = exceptionName;
    }


    public String getExceptionname() {
        return exceptionName;
    }

    public void setExceptionname(String exceptionName) {
        this.exceptionName = exceptionName;
    }


}