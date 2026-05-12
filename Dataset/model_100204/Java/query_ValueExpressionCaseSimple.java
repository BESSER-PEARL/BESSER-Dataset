





import java.util.List;
import java.util.ArrayList;

public class query_ValueExpressionCaseSimple extends ValueExpressionCase {






    private query_ValueExpressionCaseSimpleContent query_valueexpressioncasesimplecontent;




    private query_QueryValueExpression query_queryvalueexpression;




    private query_QueryValueExpression query_queryvalueexpression;




    private List<query_ValueExpressionCaseSimpleContent> query_valueexpressioncasesimplecontents;


    public query_ValueExpressionCaseSimple(
    ) {
        super(
        );
        this.query_valueexpressioncasesimplecontents = new ArrayList<>();
    }

    public query_ValueExpressionCaseSimple(
        ArrayList<query_ValueExpressionCaseSimpleContent> query_valueexpressioncasesimplecontents    ) {
        this.query_valueexpressioncasesimplecontents = query_valueexpressioncasesimplecontents;
    }


    public query_ValueExpressionCaseSimpleContent getQuery_valueexpressioncasesimplecontent() {
        return query_valueexpressioncasesimplecontent;
    }

    public void setQuery_valueexpressioncasesimplecontent(query_ValueExpressionCaseSimpleContent query_valueexpressioncasesimplecontent) {
        this.query_valueexpressioncasesimplecontent = query_valueexpressioncasesimplecontent;
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public List<query_ValueExpressionCaseSimpleContent> getQuery_valueexpressioncasesimplecontents() {
        return query_valueexpressioncasesimplecontents;
    }

    public void addQuery_valueexpressioncasesimplecontent(Query_valueexpressioncasesimplecontent query_valueexpressioncasesimplecontent) {
        this.query_valueexpressioncasesimplecontents.add(query_valueexpressioncasesimplecontent);
    }

}