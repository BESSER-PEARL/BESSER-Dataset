





import java.util.List;
import java.util.ArrayList;

public class sql_Select extends SelectQuery {

    private String select;





    private List<sql_SelectSubSet> sql_selectsubsets;




    private sql_Limit sql_limit;




    private sql_FetchFirst sql_fetchfirst;




    private sql_Offset sql_offset;




    private sql_OrColumn sql_orcolumn;




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
    public sql_Limit getSql_limit() {
        return sql_limit;
    }

    public void setSql_limit(sql_Limit sql_limit) {
        this.sql_limit = sql_limit;
    }
    public sql_FetchFirst getSql_fetchfirst() {
        return sql_fetchfirst;
    }

    public void setSql_fetchfirst(sql_FetchFirst sql_fetchfirst) {
        this.sql_fetchfirst = sql_fetchfirst;
    }
    public sql_Offset getSql_offset() {
        return sql_offset;
    }

    public void setSql_offset(sql_Offset sql_offset) {
        this.sql_offset = sql_offset;
    }
    public sql_OrColumn getSql_orcolumn() {
        return sql_orcolumn;
    }

    public void setSql_orcolumn(sql_OrColumn sql_orcolumn) {
        this.sql_orcolumn = sql_orcolumn;
    }
    public sql_SelectSubSet getSql_selectsubset() {
        return sql_selectsubset;
    }

    public void setSql_selectsubset(sql_SelectSubSet sql_selectsubset) {
        this.sql_selectsubset = sql_selectsubset;
    }

}