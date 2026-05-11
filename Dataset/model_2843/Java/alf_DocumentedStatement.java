





import java.util.List;
import java.util.ArrayList;

public class alf_DocumentedStatement  {

    private String comment;





    private alf_Statement alf_statement;




    private alf_StatementSequence alf_statementsequence;


    public alf_DocumentedStatement(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public alf_Statement getAlf_statement() {
        return alf_statement;
    }

    public void setAlf_statement(alf_Statement alf_statement) {
        this.alf_statement = alf_statement;
    }
    public alf_StatementSequence getAlf_statementsequence() {
        return alf_statementsequence;
    }

    public void setAlf_statementsequence(alf_StatementSequence alf_statementsequence) {
        this.alf_statementsequence = alf_statementsequence;
    }

}