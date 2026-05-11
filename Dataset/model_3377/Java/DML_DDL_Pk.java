





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Pk  {

    private String namePk;
    private String columnName;



    public DML_DDL_Pk(
        String namePk,        String columnName    ) {
        this.namePk = namePk;
        this.columnName = columnName;
    }


    public String getNamepk() {
        return namePk;
    }

    public void setNamepk(String namePk) {
        this.namePk = namePk;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }


}