





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_OrderingTerm  {

    private boolean desc;
    private boolean asc;





    private sqliteModel_OrderingTermList sqlitemodel_orderingtermlist;




    private sqliteModel_Expression sqlitemodel_expression;


    public sqliteModel_OrderingTerm(
        boolean desc,        boolean asc    ) {
        this.desc = desc;
        this.asc = asc;
    }


    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }
    public boolean getAsc() {
        return asc;
    }

    public void setAsc(boolean asc) {
        this.asc = asc;
    }

    public sqliteModel_OrderingTermList getSqlitemodel_orderingtermlist() {
        return sqlitemodel_orderingtermlist;
    }

    public void setSqlitemodel_orderingtermlist(sqliteModel_OrderingTermList sqlitemodel_orderingtermlist) {
        this.sqlitemodel_orderingtermlist = sqlitemodel_orderingtermlist;
    }
    public sqliteModel_Expression getSqlitemodel_expression() {
        return sqlitemodel_expression;
    }

    public void setSqlitemodel_expression(sqliteModel_Expression sqlitemodel_expression) {
        this.sqlitemodel_expression = sqlitemodel_expression;
    }

}