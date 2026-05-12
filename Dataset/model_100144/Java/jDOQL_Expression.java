





import java.util.List;
import java.util.ArrayList;

public class jDOQL_Expression extends OrderBySpec, ResultSpec {

    private String literal;
    private String name;
    private String this;
    private String castType;
    private String direction;
    private boolean isDistinct;
    private String id;
    private String unaryOperator;
    private String parameterName;





    private jDOQL_RangeClause jdoql_rangeclause;




    private jDOQL_SubqueryResultClause jdoql_subqueryresultclause;




    private jDOQL_ConditionalOrExpression jdoql_conditionalorexpression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_SimpleAndExpression jdoql_simpleandexpression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_SimpleOrExpression jdoql_simpleorexpression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_GroupByClause jdoql_groupbyclause;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_ComparisonOperatorExpression jdoql_comparisonoperatorexpression;




    private jDOQL_FieldAccessExpression jdoql_fieldaccessexpression;




    private jDOQL_MultiplicationExpression jdoql_multiplicationexpression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_SubqueryFromClause jdoql_subqueryfromclause;




    private jDOQL_WhereClause jdoql_whereclause;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_RangeClause jdoql_rangeclause;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_AdditionExpression jdoql_additionexpression;




    private jDOQL_ConditionalAndExpression jdoql_conditionalandexpression;




    private jDOQL_Expression jdoql_expression;




    private jDOQL_Expression jdoql_expression;


    public jDOQL_Expression(
        String literal,        String name,        String this,        String castType,        String direction,        boolean isDistinct,        String id,        String unaryOperator,        String parameterName    ) {
        super(
        );
        this.literal = literal;
        this.name = name;
        this.this = this;
        this.castType = castType;
        this.direction = direction;
        this.isDistinct = isDistinct;
        this.id = id;
        this.unaryOperator = unaryOperator;
        this.parameterName = parameterName;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getThis() {
        return this;
    }

    public void setThis(String this) {
        this.this = this;
    }
    public String getCasttype() {
        return castType;
    }

    public void setCasttype(String castType) {
        this.castType = castType;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getUnaryoperator() {
        return unaryOperator;
    }

    public void setUnaryoperator(String unaryOperator) {
        this.unaryOperator = unaryOperator;
    }
    public String getParametername() {
        return parameterName;
    }

    public void setParametername(String parameterName) {
        this.parameterName = parameterName;
    }

    public jDOQL_RangeClause getJdoql_rangeclause() {
        return jdoql_rangeclause;
    }

    public void setJdoql_rangeclause(jDOQL_RangeClause jdoql_rangeclause) {
        this.jdoql_rangeclause = jdoql_rangeclause;
    }
    public jDOQL_SubqueryResultClause getJdoql_subqueryresultclause() {
        return jdoql_subqueryresultclause;
    }

    public void setJdoql_subqueryresultclause(jDOQL_SubqueryResultClause jdoql_subqueryresultclause) {
        this.jdoql_subqueryresultclause = jdoql_subqueryresultclause;
    }
    public jDOQL_ConditionalOrExpression getJdoql_conditionalorexpression() {
        return jdoql_conditionalorexpression;
    }

    public void setJdoql_conditionalorexpression(jDOQL_ConditionalOrExpression jdoql_conditionalorexpression) {
        this.jdoql_conditionalorexpression = jdoql_conditionalorexpression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_SimpleAndExpression getJdoql_simpleandexpression() {
        return jdoql_simpleandexpression;
    }

    public void setJdoql_simpleandexpression(jDOQL_SimpleAndExpression jdoql_simpleandexpression) {
        this.jdoql_simpleandexpression = jdoql_simpleandexpression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_SimpleOrExpression getJdoql_simpleorexpression() {
        return jdoql_simpleorexpression;
    }

    public void setJdoql_simpleorexpression(jDOQL_SimpleOrExpression jdoql_simpleorexpression) {
        this.jdoql_simpleorexpression = jdoql_simpleorexpression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_GroupByClause getJdoql_groupbyclause() {
        return jdoql_groupbyclause;
    }

    public void setJdoql_groupbyclause(jDOQL_GroupByClause jdoql_groupbyclause) {
        this.jdoql_groupbyclause = jdoql_groupbyclause;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_ComparisonOperatorExpression getJdoql_comparisonoperatorexpression() {
        return jdoql_comparisonoperatorexpression;
    }

    public void setJdoql_comparisonoperatorexpression(jDOQL_ComparisonOperatorExpression jdoql_comparisonoperatorexpression) {
        this.jdoql_comparisonoperatorexpression = jdoql_comparisonoperatorexpression;
    }
    public jDOQL_FieldAccessExpression getJdoql_fieldaccessexpression() {
        return jdoql_fieldaccessexpression;
    }

    public void setJdoql_fieldaccessexpression(jDOQL_FieldAccessExpression jdoql_fieldaccessexpression) {
        this.jdoql_fieldaccessexpression = jdoql_fieldaccessexpression;
    }
    public jDOQL_MultiplicationExpression getJdoql_multiplicationexpression() {
        return jdoql_multiplicationexpression;
    }

    public void setJdoql_multiplicationexpression(jDOQL_MultiplicationExpression jdoql_multiplicationexpression) {
        this.jdoql_multiplicationexpression = jdoql_multiplicationexpression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_SubqueryFromClause getJdoql_subqueryfromclause() {
        return jdoql_subqueryfromclause;
    }

    public void setJdoql_subqueryfromclause(jDOQL_SubqueryFromClause jdoql_subqueryfromclause) {
        this.jdoql_subqueryfromclause = jdoql_subqueryfromclause;
    }
    public jDOQL_WhereClause getJdoql_whereclause() {
        return jdoql_whereclause;
    }

    public void setJdoql_whereclause(jDOQL_WhereClause jdoql_whereclause) {
        this.jdoql_whereclause = jdoql_whereclause;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_RangeClause getJdoql_rangeclause() {
        return jdoql_rangeclause;
    }

    public void setJdoql_rangeclause(jDOQL_RangeClause jdoql_rangeclause) {
        this.jdoql_rangeclause = jdoql_rangeclause;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_AdditionExpression getJdoql_additionexpression() {
        return jdoql_additionexpression;
    }

    public void setJdoql_additionexpression(jDOQL_AdditionExpression jdoql_additionexpression) {
        this.jdoql_additionexpression = jdoql_additionexpression;
    }
    public jDOQL_ConditionalAndExpression getJdoql_conditionalandexpression() {
        return jdoql_conditionalandexpression;
    }

    public void setJdoql_conditionalandexpression(jDOQL_ConditionalAndExpression jdoql_conditionalandexpression) {
        this.jdoql_conditionalandexpression = jdoql_conditionalandexpression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }
    public jDOQL_Expression getJdoql_expression() {
        return jdoql_expression;
    }

    public void setJdoql_expression(jDOQL_Expression jdoql_expression) {
        this.jdoql_expression = jdoql_expression;
    }

}