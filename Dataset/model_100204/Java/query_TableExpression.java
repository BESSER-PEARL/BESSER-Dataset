





import java.util.List;
import java.util.ArrayList;

public class query_TableExpression extends TableReference {






    private query_TableCorrelation query_tablecorrelation;




    private List<query_ValueExpressionColumn> query_valueexpressioncolumns;




    private query_ValueExpressionColumn query_valueexpressioncolumn;




    private List<query_ValueExpressionColumn> query_valueexpressioncolumns;




    private query_TableCorrelation query_tablecorrelation;




    private query_MergeTargetTable query_mergetargettable;




    private query_ValueExpressionColumn query_valueexpressioncolumn;




    private query_MergeTargetTable query_mergetargettable;


    public query_TableExpression(
    ) {
        super(
        );
        this.query_valueexpressioncolumns = new ArrayList<>();
        this.query_valueexpressioncolumns = new ArrayList<>();
    }

    public query_TableExpression(
        ArrayList<query_ValueExpressionColumn> query_valueexpressioncolumns,        ArrayList<query_ValueExpressionColumn> query_valueexpressioncolumns    ) {
        this.query_valueexpressioncolumns = query_valueexpressioncolumns;
        this.query_valueexpressioncolumns = query_valueexpressioncolumns;
    }


    public query_TableCorrelation getQuery_tablecorrelation() {
        return query_tablecorrelation;
    }

    public void setQuery_tablecorrelation(query_TableCorrelation query_tablecorrelation) {
        this.query_tablecorrelation = query_tablecorrelation;
    }
    public List<query_ValueExpressionColumn> getQuery_valueexpressioncolumns() {
        return query_valueexpressioncolumns;
    }

    public void addQuery_valueexpressioncolumn(Query_valueexpressioncolumn query_valueexpressioncolumn) {
        this.query_valueexpressioncolumns.add(query_valueexpressioncolumn);
    }
    public query_ValueExpressionColumn getQuery_valueexpressioncolumn() {
        return query_valueexpressioncolumn;
    }

    public void setQuery_valueexpressioncolumn(query_ValueExpressionColumn query_valueexpressioncolumn) {
        this.query_valueexpressioncolumn = query_valueexpressioncolumn;
    }
    public List<query_ValueExpressionColumn> getQuery_valueexpressioncolumns() {
        return query_valueexpressioncolumns;
    }

    public void addQuery_valueexpressioncolumn(Query_valueexpressioncolumn query_valueexpressioncolumn) {
        this.query_valueexpressioncolumns.add(query_valueexpressioncolumn);
    }
    public query_TableCorrelation getQuery_tablecorrelation() {
        return query_tablecorrelation;
    }

    public void setQuery_tablecorrelation(query_TableCorrelation query_tablecorrelation) {
        this.query_tablecorrelation = query_tablecorrelation;
    }
    public query_MergeTargetTable getQuery_mergetargettable() {
        return query_mergetargettable;
    }

    public void setQuery_mergetargettable(query_MergeTargetTable query_mergetargettable) {
        this.query_mergetargettable = query_mergetargettable;
    }
    public query_ValueExpressionColumn getQuery_valueexpressioncolumn() {
        return query_valueexpressioncolumn;
    }

    public void setQuery_valueexpressioncolumn(query_ValueExpressionColumn query_valueexpressioncolumn) {
        this.query_valueexpressioncolumn = query_valueexpressioncolumn;
    }
    public query_MergeTargetTable getQuery_mergetargettable() {
        return query_mergetargettable;
    }

    public void setQuery_mergetargettable(query_MergeTargetTable query_mergetargettable) {
        this.query_mergetargettable = query_mergetargettable;
    }

}