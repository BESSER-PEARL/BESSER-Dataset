





import java.util.List;
import java.util.ArrayList;

public class amethyst_DefinitionDeclaration extends Symbol {

    private boolean static;





    private List<amethyst_Symbol> amethyst_symbols;




    private List<amethyst_Statement> amethyst_statements;




    private amethyst_AbstractType amethyst_abstracttype;


    public amethyst_DefinitionDeclaration(
        boolean static    ) {
        super(
        );
        this.static = static;
        this.amethyst_symbols = new ArrayList<>();
        this.amethyst_statements = new ArrayList<>();
    }

    public amethyst_DefinitionDeclaration(
        boolean static        ArrayList<amethyst_Symbol> amethyst_symbols,        ArrayList<amethyst_Statement> amethyst_statements    ) {
        this.static = static;
        this.amethyst_symbols = amethyst_symbols;
        this.amethyst_statements = amethyst_statements;
    }

    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public List<amethyst_Symbol> getAmethyst_symbols() {
        return amethyst_symbols;
    }

    public void addAmethyst_symbol(Amethyst_symbol amethyst_symbol) {
        this.amethyst_symbols.add(amethyst_symbol);
    }
    public List<amethyst_Statement> getAmethyst_statements() {
        return amethyst_statements;
    }

    public void addAmethyst_statement(Amethyst_statement amethyst_statement) {
        this.amethyst_statements.add(amethyst_statement);
    }
    public amethyst_AbstractType getAmethyst_abstracttype() {
        return amethyst_abstracttype;
    }

    public void setAmethyst_abstracttype(amethyst_AbstractType amethyst_abstracttype) {
        this.amethyst_abstracttype = amethyst_abstracttype;
    }

}