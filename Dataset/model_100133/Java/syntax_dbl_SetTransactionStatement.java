





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_SetTransactionStatement extends BindingStatement {

    private String isolationLevel;
    private String rwOperation;



    public syntax_dbl_SetTransactionStatement(
        String isolationLevel,        String rwOperation    ) {
        super(
        );
        this.isolationLevel = isolationLevel;
        this.rwOperation = rwOperation;
    }


    public String getIsolationlevel() {
        return isolationLevel;
    }

    public void setIsolationlevel(String isolationLevel) {
        this.isolationLevel = isolationLevel;
    }
    public String getRwoperation() {
        return rwOperation;
    }

    public void setRwoperation(String rwOperation) {
        this.rwOperation = rwOperation;
    }


}