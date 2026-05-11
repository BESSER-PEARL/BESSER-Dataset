





import java.util.List;
import java.util.ArrayList;

public class DDL_Fk extends NamedElement {

    private String columnReference;
    private String columnName;





    private DDL_Table ddl_table;




    private DDL_Table ddl_table;


    public DDL_Fk(
        String columnReference,        String columnName    ) {
        super(
        );
        this.columnReference = columnReference;
        this.columnName = columnName;
    }


    public String getColumnreference() {
        return columnReference;
    }

    public void setColumnreference(String columnReference) {
        this.columnReference = columnReference;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }
    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }

}