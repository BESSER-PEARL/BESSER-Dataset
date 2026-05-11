





import java.util.List;
import java.util.ArrayList;

public class DML_InsertInto  {

    private String tableName;





    private DML_InsertsStatements dml_insertsstatements;


    public DML_InsertInto(
        String tableName    ) {
        this.tableName = tableName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }

    public DML_InsertsStatements getDml_insertsstatements() {
        return dml_insertsstatements;
    }

    public void setDml_insertsstatements(DML_InsertsStatements dml_insertsstatements) {
        this.dml_insertsstatements = dml_insertsstatements;
    }

}