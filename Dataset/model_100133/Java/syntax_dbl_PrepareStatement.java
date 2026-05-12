





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_PrepareStatement extends BindingStatement {

    private String statementName;
    private String from_;



    public syntax_dbl_PrepareStatement(
        String statementName,        String from_    ) {
        super(
        );
        this.statementName = statementName;
        this.from_ = from_;
    }


    public String getStatementname() {
        return statementName;
    }

    public void setStatementname(String statementName) {
        this.statementName = statementName;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }


}