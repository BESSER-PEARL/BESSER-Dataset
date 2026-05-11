





import java.util.List;
import java.util.ArrayList;

public class sql_abc extends FromValuesColumnNames {






    private List<sql_ColumnNames> sql_columnnamess;


    public sql_abc(
    ) {
        super(
        );
        this.sql_columnnamess = new ArrayList<>();
    }

    public sql_abc(
        ArrayList<sql_ColumnNames> sql_columnnamess    ) {
        this.sql_columnnamess = sql_columnnamess;
    }


    public List<sql_ColumnNames> getSql_columnnamess() {
        return sql_columnnamess;
    }

    public void addSql_columnnames(Sql_columnnames sql_columnnames) {
        this.sql_columnnamess.add(sql_columnnames);
    }

}