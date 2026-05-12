





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_OrderingTermList  {






    private List<sqliteModel_OrderingTerm> sqlitemodel_orderingterms;




    private sqliteModel_SelectStatement sqlitemodel_selectstatement;


    public sqliteModel_OrderingTermList(
    ) {
        this.sqlitemodel_orderingterms = new ArrayList<>();
    }

    public sqliteModel_OrderingTermList(
        ArrayList<sqliteModel_OrderingTerm> sqlitemodel_orderingterms    ) {
        this.sqlitemodel_orderingterms = sqlitemodel_orderingterms;
    }


    public List<sqliteModel_OrderingTerm> getSqlitemodel_orderingterms() {
        return sqlitemodel_orderingterms;
    }

    public void addSqlitemodel_orderingterm(Sqlitemodel_orderingterm sqlitemodel_orderingterm) {
        this.sqlitemodel_orderingterms.add(sqlitemodel_orderingterm);
    }
    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }

}