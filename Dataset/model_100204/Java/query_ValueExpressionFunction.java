





import java.util.List;
import java.util.ArrayList;

public class query_ValueExpressionFunction extends ValueExpressionAtomic {

    private boolean columnFunction;
    private boolean distinct;
    private boolean specialRegister;





    private List<query_QueryValueExpression> query_queryvalueexpressions;




    private query_QueryValueExpression query_queryvalueexpression;


    public query_ValueExpressionFunction(
        boolean columnFunction,        boolean distinct,        boolean specialRegister    ) {
        super(
        );
        this.columnFunction = columnFunction;
        this.distinct = distinct;
        this.specialRegister = specialRegister;
        this.query_queryvalueexpressions = new ArrayList<>();
    }

    public query_ValueExpressionFunction(
        boolean columnFunction,        boolean distinct,        boolean specialRegister        ArrayList<query_QueryValueExpression> query_queryvalueexpressions    ) {
        this.columnFunction = columnFunction;
        this.distinct = distinct;
        this.specialRegister = specialRegister;
        this.query_queryvalueexpressions = query_queryvalueexpressions;
    }

    public boolean getColumnfunction() {
        return columnFunction;
    }

    public void setColumnfunction(boolean columnFunction) {
        this.columnFunction = columnFunction;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public boolean getSpecialregister() {
        return specialRegister;
    }

    public void setSpecialregister(boolean specialRegister) {
        this.specialRegister = specialRegister;
    }

    public List<query_QueryValueExpression> getQuery_queryvalueexpressions() {
        return query_queryvalueexpressions;
    }

    public void addQuery_queryvalueexpression(Query_queryvalueexpression query_queryvalueexpression) {
        this.query_queryvalueexpressions.add(query_queryvalueexpression);
    }
    public query_QueryValueExpression getQuery_queryvalueexpression() {
        return query_queryvalueexpression;
    }

    public void setQuery_queryvalueexpression(query_QueryValueExpression query_queryvalueexpression) {
        this.query_queryvalueexpression = query_queryvalueexpression;
    }

}