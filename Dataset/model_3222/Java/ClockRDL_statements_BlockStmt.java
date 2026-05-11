





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_statements_BlockStmt extends Statement {






    private List<kernel_Statement> kernel_statements;


    public ClockRDL_statements_BlockStmt(
    ) {
        super(
        );
        this.kernel_statements = new ArrayList<>();
    }

    public ClockRDL_statements_BlockStmt(
        ArrayList<kernel_Statement> kernel_statements    ) {
        this.kernel_statements = kernel_statements;
    }


    public List<kernel_Statement> getKernel_statements() {
        return kernel_statements;
    }

    public void addKernel_statement(Kernel_statement kernel_statement) {
        this.kernel_statements.add(kernel_statement);
    }

}