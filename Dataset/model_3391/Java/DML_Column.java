





import java.util.List;
import java.util.ArrayList;

public class DML_Column  {

    private String columnName;





    private DML_InsertInto dml_insertinto;


    public DML_Column(
        String columnName    ) {
        this.columnName = columnName;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public DML_InsertInto getDml_insertinto() {
        return dml_insertinto;
    }

    public void setDml_insertinto(DML_InsertInto dml_insertinto) {
        this.dml_insertinto = dml_insertinto;
    }

}