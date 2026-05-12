





import java.util.List;
import java.util.ArrayList;

public class stext_ReactionEffect extends Effect {






    private List<stext_Statement> stext_statements;


    public stext_ReactionEffect(
    ) {
        super(
        );
        this.stext_statements = new ArrayList<>();
    }

    public stext_ReactionEffect(
        ArrayList<stext_Statement> stext_statements    ) {
        this.stext_statements = stext_statements;
    }


    public List<stext_Statement> getStext_statements() {
        return stext_statements;
    }

    public void addStext_statement(Stext_statement stext_statement) {
        this.stext_statements.add(stext_statement);
    }

}