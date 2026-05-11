





import java.util.List;
import java.util.ArrayList;

public class robochart_SeqStatement extends Statement {






    private List<robochart_Statement> robochart_statements;


    public robochart_SeqStatement(
    ) {
        super(
        );
        this.robochart_statements = new ArrayList<>();
    }

    public robochart_SeqStatement(
        ArrayList<robochart_Statement> robochart_statements    ) {
        this.robochart_statements = robochart_statements;
    }


    public List<robochart_Statement> getRobochart_statements() {
        return robochart_statements;
    }

    public void addRobochart_statement(Robochart_statement robochart_statement) {
        this.robochart_statements.add(robochart_statement);
    }

}