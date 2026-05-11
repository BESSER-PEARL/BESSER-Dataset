





import java.util.List;
import java.util.ArrayList;

public class amethyst_ForStatement extends Statement {






    private amethyst_Symbol amethyst_symbol;




    private List<amethyst_Statement> amethyst_statements;


    public amethyst_ForStatement(
    ) {
        super(
        );
        this.amethyst_statements = new ArrayList<>();
    }

    public amethyst_ForStatement(
        ArrayList<amethyst_Statement> amethyst_statements    ) {
        this.amethyst_statements = amethyst_statements;
    }


    public amethyst_Symbol getAmethyst_symbol() {
        return amethyst_symbol;
    }

    public void setAmethyst_symbol(amethyst_Symbol amethyst_symbol) {
        this.amethyst_symbol = amethyst_symbol;
    }
    public List<amethyst_Statement> getAmethyst_statements() {
        return amethyst_statements;
    }

    public void addAmethyst_statement(Amethyst_statement amethyst_statement) {
        this.amethyst_statements.add(amethyst_statement);
    }

}