





import java.util.List;
import java.util.ArrayList;

public class sql_WhenList extends SQLCaseWhens {






    private List<sql_SqlCaseWhen> sql_sqlcasewhens;


    public sql_WhenList(
    ) {
        super(
        );
        this.sql_sqlcasewhens = new ArrayList<>();
    }

    public sql_WhenList(
        ArrayList<sql_SqlCaseWhen> sql_sqlcasewhens    ) {
        this.sql_sqlcasewhens = sql_sqlcasewhens;
    }


    public List<sql_SqlCaseWhen> getSql_sqlcasewhens() {
        return sql_sqlcasewhens;
    }

    public void addSql_sqlcasewhen(Sql_sqlcasewhen sql_sqlcasewhen) {
        this.sql_sqlcasewhens.add(sql_sqlcasewhen);
    }

}