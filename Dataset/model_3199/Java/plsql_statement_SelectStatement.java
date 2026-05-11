





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_SelectStatement extends ModifySQLStatement {

    private boolean collect;
    private boolean all;
    private String from_;
    private String selectList;
    private boolean unique;
    private boolean isCount;
    private boolean bulk;
    private boolean distinct;





    private List<Expression> expressions;




    private List<VarRefExpression> varrefexpressions;


    public plsql_statement_SelectStatement(
        boolean collect,        boolean all,        String from_,        String selectList,        boolean unique,        boolean isCount,        boolean bulk,        boolean distinct    ) {
        super(
        );
        this.collect = collect;
        this.all = all;
        this.from_ = from_;
        this.selectList = selectList;
        this.unique = unique;
        this.isCount = isCount;
        this.bulk = bulk;
        this.distinct = distinct;
        this.expressions = new ArrayList<>();
        this.varrefexpressions = new ArrayList<>();
    }

    public plsql_statement_SelectStatement(
        boolean collect,        boolean all,        String from_,        String selectList,        boolean unique,        boolean isCount,        boolean bulk,        boolean distinct        ArrayList<Expression> expressions,        ArrayList<VarRefExpression> varrefexpressions    ) {
        this.collect = collect;
        this.all = all;
        this.from_ = from_;
        this.selectList = selectList;
        this.unique = unique;
        this.isCount = isCount;
        this.bulk = bulk;
        this.distinct = distinct;
        this.expressions = expressions;
        this.varrefexpressions = varrefexpressions;
    }

    public boolean getCollect() {
        return collect;
    }

    public void setCollect(boolean collect) {
        this.collect = collect;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getSelectlist() {
        return selectList;
    }

    public void setSelectlist(String selectList) {
        this.selectList = selectList;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getIscount() {
        return isCount;
    }

    public void setIscount(boolean isCount) {
        this.isCount = isCount;
    }
    public boolean getBulk() {
        return bulk;
    }

    public void setBulk(boolean bulk) {
        this.bulk = bulk;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }
    public List<VarRefExpression> getVarrefexpressions() {
        return varrefexpressions;
    }

    public void addVarrefexpression(Varrefexpression varrefexpression) {
        this.varrefexpressions.add(varrefexpression);
    }

}