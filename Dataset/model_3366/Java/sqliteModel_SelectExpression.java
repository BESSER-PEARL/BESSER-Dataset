





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_SelectExpression extends SelectCoreExpression {

    private boolean allColumns;
    private boolean all;
    private boolean distinct;





    private sqliteModel_HavingExpressions sqlitemodel_havingexpressions;




    private sqliteModel_JoinSource sqlitemodel_joinsource;




    private sqliteModel_GroupByExpressions sqlitemodel_groupbyexpressions;




    private sqliteModel_WhereExpressions sqlitemodel_whereexpressions;




    private sqliteModel_SelectList sqlitemodel_selectlist;


    public sqliteModel_SelectExpression(
        boolean allColumns,        boolean all,        boolean distinct    ) {
        super(
        );
        this.allColumns = allColumns;
        this.all = all;
        this.distinct = distinct;
    }


    public boolean getAllcolumns() {
        return allColumns;
    }

    public void setAllcolumns(boolean allColumns) {
        this.allColumns = allColumns;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public sqliteModel_HavingExpressions getSqlitemodel_havingexpressions() {
        return sqlitemodel_havingexpressions;
    }

    public void setSqlitemodel_havingexpressions(sqliteModel_HavingExpressions sqlitemodel_havingexpressions) {
        this.sqlitemodel_havingexpressions = sqlitemodel_havingexpressions;
    }
    public sqliteModel_JoinSource getSqlitemodel_joinsource() {
        return sqlitemodel_joinsource;
    }

    public void setSqlitemodel_joinsource(sqliteModel_JoinSource sqlitemodel_joinsource) {
        this.sqlitemodel_joinsource = sqlitemodel_joinsource;
    }
    public sqliteModel_GroupByExpressions getSqlitemodel_groupbyexpressions() {
        return sqlitemodel_groupbyexpressions;
    }

    public void setSqlitemodel_groupbyexpressions(sqliteModel_GroupByExpressions sqlitemodel_groupbyexpressions) {
        this.sqlitemodel_groupbyexpressions = sqlitemodel_groupbyexpressions;
    }
    public sqliteModel_WhereExpressions getSqlitemodel_whereexpressions() {
        return sqlitemodel_whereexpressions;
    }

    public void setSqlitemodel_whereexpressions(sqliteModel_WhereExpressions sqlitemodel_whereexpressions) {
        this.sqlitemodel_whereexpressions = sqlitemodel_whereexpressions;
    }
    public sqliteModel_SelectList getSqlitemodel_selectlist() {
        return sqlitemodel_selectlist;
    }

    public void setSqlitemodel_selectlist(sqliteModel_SelectList sqlitemodel_selectlist) {
        this.sqlitemodel_selectlist = sqlitemodel_selectlist;
    }

}