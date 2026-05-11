





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Pk  {

    private String columnName;
    private String namePk;



    public DML_DDL_Pk(
        String columnName,        String namePk    ) {
        this.columnName = columnName;
        this.namePk = namePk;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getNamepk() {
        return namePk;
    }

    public void setNamepk(String namePk) {
        this.namePk = namePk;
    }


}