





import java.util.List;
import java.util.ArrayList;

public class amethyst_WhenStatement extends Statement {






    private List<amethyst_Statement> amethyst_statements;


    public amethyst_WhenStatement(
    ) {
        super(
        );
        this.amethyst_statements = new ArrayList<>();
    }

    public amethyst_WhenStatement(
        ArrayList<amethyst_Statement> amethyst_statements    ) {
        this.amethyst_statements = amethyst_statements;
    }


    public List<amethyst_Statement> getAmethyst_statements() {
        return amethyst_statements;
    }

    public void addAmethyst_statement(Amethyst_statement amethyst_statement) {
        this.amethyst_statements.add(amethyst_statement);
    }

}