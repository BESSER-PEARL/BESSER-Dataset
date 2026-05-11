





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_SelectStatement extends ModifySQLStatement {

    private boolean collect;
    private boolean distinct;
    private String selectList;
    private boolean isCount;
    private String from_;
    private boolean all;
    private boolean unique;
    private boolean bulk;





    private List<VarRefExpression> varrefexpressions;




    private List<Expression> expressions;


    public plsql_statement_SelectStatement(
        boolean collect,        boolean distinct,        String selectList,        boolean isCount,        String from_,        boolean all,        boolean unique,        boolean bulk    ) {
        super(
        );
        this.collect = collect;
        this.distinct = distinct;
        this.selectList = selectList;
        this.isCount = isCount;
        this.from_ = from_;
        this.all = all;
        this.unique = unique;
        this.bulk = bulk;
        this.varrefexpressions = new ArrayList<>();
        this.expressions = new ArrayList<>();
    }

    public plsql_statement_SelectStatement(
        boolean collect,        boolean distinct,        String selectList,        boolean isCount,        String from_,        boolean all,        boolean unique,        boolean bulk        ArrayList<VarRefExpression> varrefexpressions,        ArrayList<Expression> expressions    ) {
        this.collect = collect;
        this.distinct = distinct;
        this.selectList = selectList;
        this.isCount = isCount;
        this.from_ = from_;
        this.all = all;
        this.unique = unique;
        this.bulk = bulk;
        this.varrefexpressions = varrefexpressions;
        this.expressions = expressions;
    }

    public boolean getCollect() {
        return collect;
    }

    public void setCollect(boolean collect) {
        this.collect = collect;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public String getSelectlist() {
        return selectList;
    }

    public void setSelectlist(String selectList) {
        this.selectList = selectList;
    }
    public boolean getIscount() {
        return isCount;
    }

    public void setIscount(boolean isCount) {
        this.isCount = isCount;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getBulk() {
        return bulk;
    }

    public void setBulk(boolean bulk) {
        this.bulk = bulk;
    }

    public List<VarRefExpression> getVarrefexpressions() {
        return varrefexpressions;
    }

    public void addVarrefexpression(Varrefexpression varrefexpression) {
        this.varrefexpressions.add(varrefexpression);
    }
    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}