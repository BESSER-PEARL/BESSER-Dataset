





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_While extends Statement {






    private List<dinkiemodel_Statement> dinkiemodel_statements;


    public dinkiemodel_While(
    ) {
        super(
        );
        this.dinkiemodel_statements = new ArrayList<>();
    }

    public dinkiemodel_While(
        ArrayList<dinkiemodel_Statement> dinkiemodel_statements    ) {
        this.dinkiemodel_statements = dinkiemodel_statements;
    }


    public List<dinkiemodel_Statement> getDinkiemodel_statements() {
        return dinkiemodel_statements;
    }

    public void addDinkiemodel_statement(Dinkiemodel_statement dinkiemodel_statement) {
        this.dinkiemodel_statements.add(dinkiemodel_statement);
    }

}