





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_PrepareStatement extends BindingStatement {

    private String from_;
    private String statementName;





    private IntoClause intoclause;


    public syntax_dbl_PrepareStatement(
        String from_,        String statementName    ) {
        super(
        );
        this.from_ = from_;
        this.statementName = statementName;
    }


    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getStatementname() {
        return statementName;
    }

    public void setStatementname(String statementName) {
        this.statementName = statementName;
    }

    public IntoClause getIntoclause() {
        return intoclause;
    }

    public void setIntoclause(IntoClause intoclause) {
        this.intoclause = intoclause;
    }

}