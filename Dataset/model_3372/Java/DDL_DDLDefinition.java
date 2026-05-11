





import java.util.List;
import java.util.ArrayList;

public class DDL_DDLDefinition  {






    private List<DDL_Statement> ddl_statements;




    private DDL_DataType ddl_datatype;


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
    public DDL_DataType getDdl_datatype() {
        return ddl_datatype;
    }

    public void setDdl_datatype(DDL_DataType ddl_datatype) {
        this.ddl_datatype = ddl_datatype;
    }

}