





import java.util.List;
import java.util.ArrayList;

public class sql_Select extends SelectQuery {

    private String select;





    private List<sql_SelectSubSet> sql_selectsubsets;




    private sql_FetchFirst sql_fetchfirst;




    private sql_SelectSubSet sql_selectsubset;


    public sql_Select(
        String select    ) {
        super(
        );
        this.select = select;
        this.sql_selectsubsets = new ArrayList<>();
    }

    public sql_Select(
        String select        ArrayList<sql_SelectSubSet> sql_selectsubsets    ) {
        this.select = select;
        this.sql_selectsubsets = sql_selectsubsets;
    }

    public String getSelect() {
        return select;
    }

    public void setSelect(String select) {
        this.select = select;
    }

    public List<sql_SelectSubSet> getSql_selectsubsets() {
        return sql_selectsubsets;
    }

    public void addSql_selectsubset(Sql_selectsubset sql_selectsubset) {
        this.sql_selectsubsets.add(sql_selectsubset);
    }
    public sql_FetchFirst getSql_fetchfirst() {
        return sql_fetchfirst;
    }

    public void setSql_fetchfirst(sql_FetchFirst sql_fetchfirst) {
        this.sql_fetchfirst = sql_fetchfirst;
    }
    public sql_SelectSubSet getSql_selectsubset() {
        return sql_selectsubset;
    }

    public void setSql_selectsubset(sql_SelectSubSet sql_selectsubset) {
        this.sql_selectsubset = sql_selectsubset;
    }

}