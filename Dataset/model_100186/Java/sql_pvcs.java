





import java.util.List;
import java.util.ArrayList;

public class sql_pvcs extends Pivots {






    private List<sql_PivotCol> sql_pivotcols;


    public sql_pvcs(
    ) {
        super(
        );
        this.sql_pivotcols = new ArrayList<>();
    }

    public sql_pvcs(
        ArrayList<sql_PivotCol> sql_pivotcols    ) {
        this.sql_pivotcols = sql_pivotcols;
    }


    public List<sql_PivotCol> getSql_pivotcols() {
        return sql_pivotcols;
    }

    public void addSql_pivotcol(Sql_pivotcol sql_pivotcol) {
        this.sql_pivotcols.add(sql_pivotcol);
    }

}