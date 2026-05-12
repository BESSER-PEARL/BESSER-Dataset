





import java.util.List;
import java.util.ArrayList;

public class query_MergeInsertSpecification extends MergeOperationSpecification {






    private query_ValueExpressionColumn query_valueexpressioncolumn;




    private query_ValuesRow query_valuesrow;




    private List<query_ValueExpressionColumn> query_valueexpressioncolumns;


    public query_MergeInsertSpecification(
    ) {
        super(
        );
        this.query_valueexpressioncolumns = new ArrayList<>();
    }

    public query_MergeInsertSpecification(
        ArrayList<query_ValueExpressionColumn> query_valueexpressioncolumns    ) {
        this.query_valueexpressioncolumns = query_valueexpressioncolumns;
    }


    public query_ValueExpressionColumn getQuery_valueexpressioncolumn() {
        return query_valueexpressioncolumn;
    }

    public void setQuery_valueexpressioncolumn(query_ValueExpressionColumn query_valueexpressioncolumn) {
        this.query_valueexpressioncolumn = query_valueexpressioncolumn;
    }
    public query_ValuesRow getQuery_valuesrow() {
        return query_valuesrow;
    }

    public void setQuery_valuesrow(query_ValuesRow query_valuesrow) {
        this.query_valuesrow = query_valuesrow;
    }
    public List<query_ValueExpressionColumn> getQuery_valueexpressioncolumns() {
        return query_valueexpressioncolumns;
    }

    public void addQuery_valueexpressioncolumn(Query_valueexpressioncolumn query_valueexpressioncolumn) {
        this.query_valueexpressioncolumns.add(query_valueexpressioncolumn);
    }

}