





import java.util.List;
import java.util.ArrayList;

public class core_ClosureDeclaration extends Expression {






    private List<core_Statement> core_statements;




    private List<core_ClosureParameter> core_closureparameters;


    public core_ClosureDeclaration(
    ) {
        super(
        );
        this.core_statements = new ArrayList<>();
        this.core_closureparameters = new ArrayList<>();
    }

    public core_ClosureDeclaration(
        ArrayList<core_Statement> core_statements,        ArrayList<core_ClosureParameter> core_closureparameters    ) {
        this.core_statements = core_statements;
        this.core_closureparameters = core_closureparameters;
    }


    public List<core_Statement> getCore_statements() {
        return core_statements;
    }

    public void addCore_statement(Core_statement core_statement) {
        this.core_statements.add(core_statement);
    }
    public List<core_ClosureParameter> getCore_closureparameters() {
        return core_closureparameters;
    }

    public void addCore_closureparameter(Core_closureparameter core_closureparameter) {
        this.core_closureparameters.add(core_closureparameter);
    }

}