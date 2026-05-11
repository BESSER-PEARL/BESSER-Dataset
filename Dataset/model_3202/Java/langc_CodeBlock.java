





import java.util.List;
import java.util.ArrayList;

public class langc_CodeBlock extends Statement {

    private boolean forceBraces;





    private List<langc_Statement> langc_statements;


    public langc_CodeBlock(
        boolean forceBraces    ) {
        super(
        );
        this.forceBraces = forceBraces;
        this.langc_statements = new ArrayList<>();
    }

    public langc_CodeBlock(
        boolean forceBraces        ArrayList<langc_Statement> langc_statements    ) {
        this.forceBraces = forceBraces;
        this.langc_statements = langc_statements;
    }

    public boolean getForcebraces() {
        return forceBraces;
    }

    public void setForcebraces(boolean forceBraces) {
        this.forceBraces = forceBraces;
    }

    public List<langc_Statement> getLangc_statements() {
        return langc_statements;
    }

    public void addLangc_statement(Langc_statement langc_statement) {
        this.langc_statements.add(langc_statement);
    }

}