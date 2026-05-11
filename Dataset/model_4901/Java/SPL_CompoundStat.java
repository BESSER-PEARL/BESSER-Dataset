





import java.util.List;
import java.util.ArrayList;

public class SPL_CompoundStat extends Statement {






    private List<SPL_Statement> spl_statements;


    public SPL_CompoundStat(
    ) {
        super(
        );
        this.spl_statements = new ArrayList<>();
    }

    public SPL_CompoundStat(
        ArrayList<SPL_Statement> spl_statements    ) {
        this.spl_statements = spl_statements;
    }


    public List<SPL_Statement> getSpl_statements() {
        return spl_statements;
    }

    public void addSpl_statement(Spl_statement spl_statement) {
        this.spl_statements.add(spl_statement);
    }

}