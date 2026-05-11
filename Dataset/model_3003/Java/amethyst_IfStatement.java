





import java.util.List;
import java.util.ArrayList;

public class amethyst_IfStatement extends Statement {






    private List<amethyst_Statement> amethyst_statements;




    private amethyst_Statement amethyst_statement;


    public amethyst_IfStatement(
    ) {
        super(
        );
        this.amethyst_statements = new ArrayList<>();
    }

    public amethyst_IfStatement(
        ArrayList<amethyst_Statement> amethyst_statements    ) {
        this.amethyst_statements = amethyst_statements;
    }


    public List<amethyst_Statement> getAmethyst_statements() {
        return amethyst_statements;
    }

    public void addAmethyst_statement(Amethyst_statement amethyst_statement) {
        this.amethyst_statements.add(amethyst_statement);
    }
    public amethyst_Statement getAmethyst_statement() {
        return amethyst_statement;
    }

    public void setAmethyst_statement(amethyst_Statement amethyst_statement) {
        this.amethyst_statement = amethyst_statement;
    }

}