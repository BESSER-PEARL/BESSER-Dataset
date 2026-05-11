





import java.util.List;
import java.util.ArrayList;

public class DDL_Ck extends NamedElement {

    private String columnName;



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


}