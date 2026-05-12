





import java.util.List;
import java.util.ArrayList;

public class query_CallStatement extends SQLQueryObject, statements_SQLControlStatement {






    private query_QueryValueExpression query_queryvalueexpression;




    private query_ProcedureReference query_procedurereference;




    private List<query_QueryValueExpression> query_queryvalueexpressions;




    private query_ProcedureReference query_procedurereference;


    public query_CallStatement(
    ) {
        super(
        );
        this.query_queryvalueexpressions = new ArrayList<>();
    }

    public query_CallStatement(
        ArrayList<query_QueryValueExpression> query_queryvalueexpressions    ) {
        this.query_queryvalueexpressions = query_queryvalueexpressions;
    }


    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }
    public query_ProcedureReference getQuery_procedurereference() {
        return query_procedurereference;
    }

    public void setQuery_procedurereference(query_ProcedureReference query_procedurereference) {
        this.query_procedurereference = query_procedurereference;
    }
    public List<query_QueryValueExpression> getQuery_queryvalueexpressions() {
        return query_queryvalueexpressions;
    }

    public void addQuery_queryvalueexpression(Query_queryvalueexpression query_queryvalueexpression) {
        this.query_queryvalueexpressions.add(query_queryvalueexpression);
    }
    public query_ProcedureReference getQuery_procedurereference() {
        return query_procedurereference;
    }

    public void setQuery_procedurereference(query_ProcedureReference query_procedurereference) {
        this.query_procedurereference = query_procedurereference;
    }

}