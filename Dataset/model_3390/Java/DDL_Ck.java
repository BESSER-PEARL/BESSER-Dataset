





import java.util.List;
import java.util.ArrayList;

public class DDL_Ck extends NamedElement {

    private String columnName;





    private DDL_Table ddl_table;


    public DDL_Ck(
        String columnName    ) {
        super(
        );
        this.columnName = columnName;
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

}