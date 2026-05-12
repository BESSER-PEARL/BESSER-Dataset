





import java.util.List;
import java.util.ArrayList;

public class sql_Prms  {






    private List<sql_JRParameter> sql_jrparameters;




    private sql_XExpr sql_xexpr;


    public sql_Prms(
    ) {
        this.sql_jrparameters = new ArrayList<>();
    }

    public sql_Prms(
        ArrayList<sql_JRParameter> sql_jrparameters    ) {
        this.sql_jrparameters = sql_jrparameters;
    }


    public List<sql_JRParameter> getSql_jrparameters() {
        return sql_jrparameters;
    }

    public void addSql_jrparameter(Sql_jrparameter sql_jrparameter) {
        this.sql_jrparameters.add(sql_jrparameter);
    }
    public sql_XExpr getSql_xexpr() {
        return sql_xexpr;
    }

    public void setSql_xexpr(sql_XExpr sql_xexpr) {
        this.sql_xexpr = sql_xexpr;
    }

}