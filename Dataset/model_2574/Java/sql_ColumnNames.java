





import java.util.List;
import java.util.ArrayList;

public class sql_ColumnNames extends FromValuesColumnNames {

    private String colName;





    private sql_abc sql_abc;


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

    public sql_abc getSql_abc() {
        return sql_abc;
    }

    public void setSql_abc(sql_abc sql_abc) {
        this.sql_abc = sql_abc;
    }

}