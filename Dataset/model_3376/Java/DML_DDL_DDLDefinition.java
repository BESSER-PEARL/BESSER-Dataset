





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_DDLDefinition  {






    private List<DML_DDL_Statement> dml_ddl_statements;




    private DML_DDL_DataType dml_ddl_datatype;


    public DML_DDL_DDLDefinition(
    ) {
        this.dml_ddl_statements = new ArrayList<>();
    }

    public DML_DDL_DDLDefinition(
        ArrayList<DML_DDL_Statement> dml_ddl_statements    ) {
        this.dml_ddl_statements = dml_ddl_statements;
    }


    public List<DML_DDL_Statement> getDml_ddl_statements() {
        return dml_ddl_statements;
    }

    public void addDml_ddl_statement(Dml_ddl_statement dml_ddl_statement) {
        this.dml_ddl_statements.add(dml_ddl_statement);
    }
    public DML_DDL_DataType getDml_ddl_datatype() {
        return dml_ddl_datatype;
    }

    public void setDml_ddl_datatype(DML_DDL_DataType dml_ddl_datatype) {
        this.dml_ddl_datatype = dml_ddl_datatype;
    }

}