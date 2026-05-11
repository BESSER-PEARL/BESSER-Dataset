





import java.util.List;
import java.util.ArrayList;

public class sql_ColumnNames extends FromValuesColumnNames {

    private String colName;



    public sql_ColumnNames(
        String colName    ) {
        super(
        );
        this.colName = colName;
    }


    public String getColname() {
        return colName;
    }

    public void setColname(String colName) {
        this.colName = colName;
    }


}