





import java.util.List;
import java.util.ArrayList;

public class sql_GroupByColumnFull extends OrGroupByColumn {






    private sql_OrGroupByColumn sql_orgroupbycolumn;




    private sql_ColumnFull sql_columnfull;


    public sql_GroupByColumnFull(
    ) {
        super(
        );
    }



    public sql_OrGroupByColumn getSql_orgroupbycolumn() {
        return sql_orgroupbycolumn;
    }

    public void setSql_orgroupbycolumn(sql_OrGroupByColumn sql_orgroupbycolumn) {
        this.sql_orgroupbycolumn = sql_orgroupbycolumn;
    }
    public sql_ColumnFull getSql_columnfull() {
        return sql_columnfull;
    }

    public void setSql_columnfull(sql_ColumnFull sql_columnfull) {
        this.sql_columnfull = sql_columnfull;
    }

}