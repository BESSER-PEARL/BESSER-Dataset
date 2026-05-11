





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_Sync extends Statement {

    private String varName;





    private List<dinkiemodel_Statement> dinkiemodel_statements;


    public dinkiemodel_Sync(
        String varName    ) {
        super(
        );
        this.varName = varName;
        this.dinkiemodel_statements = new ArrayList<>();
    }

    public dinkiemodel_Sync(
        String varName        ArrayList<dinkiemodel_Statement> dinkiemodel_statements    ) {
        this.varName = varName;
        this.dinkiemodel_statements = dinkiemodel_statements;
    }

    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public List<dinkiemodel_Statement> getDinkiemodel_statements() {
        return dinkiemodel_statements;
    }

    public void addDinkiemodel_statement(Dinkiemodel_statement dinkiemodel_statement) {
        this.dinkiemodel_statements.add(dinkiemodel_statement);
    }

}