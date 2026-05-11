





import java.util.List;
import java.util.ArrayList;

public class fiacre_Select extends Statement {






    private List<fiacre_Statement> fiacre_statements;


    public fiacre_Select(
    ) {
        super(
        );
        this.fiacre_statements = new ArrayList<>();
    }

    public fiacre_Select(
        ArrayList<fiacre_Statement> fiacre_statements    ) {
        this.fiacre_statements = fiacre_statements;
    }


    public List<fiacre_Statement> getFiacre_statements() {
        return fiacre_statements;
    }

    public void addFiacre_statement(Fiacre_statement fiacre_statement) {
        this.fiacre_statements.add(fiacre_statement);
    }

}