





import java.util.List;
import java.util.ArrayList;

public class astm_SwitchCase extends OtherSyntaxObject {






    private List<astm_Statement> astm_statements;


    public astm_SwitchCase(
    ) {
        super(
        );
        this.astm_statements = new ArrayList<>();
    }

    public astm_SwitchCase(
        ArrayList<astm_Statement> astm_statements    ) {
        this.astm_statements = astm_statements;
    }


    public List<astm_Statement> getAstm_statements() {
        return astm_statements;
    }

    public void addAstm_statement(Astm_statement astm_statement) {
        this.astm_statements.add(astm_statement);
    }

}