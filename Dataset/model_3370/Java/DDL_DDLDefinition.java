





import java.util.List;
import java.util.ArrayList;

public class DDL_DDLDefinition  {






    private List<DDL_Statement> ddl_statements;


    public DDL_DDLDefinition(
    ) {
        this.ddl_statements = new ArrayList<>();
    }

    public DDL_DDLDefinition(
        ArrayList<DDL_Statement> ddl_statements    ) {
        this.ddl_statements = ddl_statements;
    }


    public List<DDL_Statement> getDdl_statements() {
        return ddl_statements;
    }

    public void addDdl_statement(Ddl_statement ddl_statement) {
        this.ddl_statements.add(ddl_statement);
    }

}