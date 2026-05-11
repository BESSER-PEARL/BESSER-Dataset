





import java.util.List;
import java.util.ArrayList;

public class DDL_Column extends NamedElement {

    private boolean columnNull;





    private DDL_Type ddl_type;




    private DDL_Table ddl_table;


    public DDL_Column(
        boolean columnNull    ) {
        super(
        );
        this.columnNull = columnNull;
    }


    public boolean getColumnnull() {
        return columnNull;
    }

    public void setColumnnull(boolean columnNull) {
        this.columnNull = columnNull;
    }

    public DDL_Type getDdl_type() {
        return ddl_type;
    }

    public void setDdl_type(DDL_Type ddl_type) {
        this.ddl_type = ddl_type;
    }
    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }

}