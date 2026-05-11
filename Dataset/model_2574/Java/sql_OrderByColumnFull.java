





import java.util.List;
import java.util.ArrayList;

public class sql_OrderByColumnFull extends OrOrderByColumn {

    private String direction;
    private String colOrderInt;





    private sql_ColumnFull sql_columnfull;




    private sql_OrOrderByColumn sql_ororderbycolumn;


    public sql_OrderByColumnFull(
        String direction,        String colOrderInt    ) {
        super(
        );
        this.direction = direction;
        this.colOrderInt = colOrderInt;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getColorderint() {
        return colOrderInt;
    }

    public void setColorderint(String colOrderInt) {
        this.colOrderInt = colOrderInt;
    }

    public sql_ColumnFull getSql_columnfull() {
        return sql_columnfull;
    }

    public void setSql_columnfull(sql_ColumnFull sql_columnfull) {
        this.sql_columnfull = sql_columnfull;
    }
    public sql_OrOrderByColumn getSql_ororderbycolumn() {
        return sql_ororderbycolumn;
    }

    public void setSql_ororderbycolumn(sql_OrOrderByColumn sql_ororderbycolumn) {
        this.sql_ororderbycolumn = sql_ororderbycolumn;
    }

}