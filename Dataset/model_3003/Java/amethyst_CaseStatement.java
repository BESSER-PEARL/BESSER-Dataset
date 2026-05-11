





import java.util.List;
import java.util.ArrayList;

public class amethyst_CaseStatement extends Statement {






    private amethyst_Statement amethyst_statement;




    private List<amethyst_Statement> amethyst_statements;


    public amethyst_CaseStatement(
    ) {
        super(
        );
        this.amethyst_statements = new ArrayList<>();
    }

    public amethyst_CaseStatement(
        ArrayList<amethyst_Statement> amethyst_statements    ) {
        this.amethyst_statements = amethyst_statements;
    }


    public amethyst_Statement getAmethyst_statement() {
        return amethyst_statement;
    }

    public void setAmethyst_statement(amethyst_Statement amethyst_statement) {
        this.amethyst_statement = amethyst_statement;
    }
    public List<amethyst_Statement> getAmethyst_statements() {
        return amethyst_statements;
    }

    public void addAmethyst_statement(Amethyst_statement amethyst_statement) {
        this.amethyst_statements.add(amethyst_statement);
    }

}