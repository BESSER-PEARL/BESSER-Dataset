





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_SelectStatement extends ModifySQLStatement {

    private boolean unique;
    private boolean bulk;
    private String selectList;
    private boolean isCount;
    private String from_;
    private boolean collect;
    private boolean distinct;
    private boolean all;





    private List<Expression> expressions;




    private List<VarRefExpression> varrefexpressions;


    public plsql_statement_SelectStatement(
        boolean unique,        boolean bulk,        String selectList,        boolean isCount,        String from_,        boolean collect,        boolean distinct,        boolean all    ) {
        super(
        );
        this.unique = unique;
        this.bulk = bulk;
        this.selectList = selectList;
        this.isCount = isCount;
        this.from_ = from_;
        this.collect = collect;
        this.distinct = distinct;
        this.all = all;
        this.expressions = new ArrayList<>();
        this.varrefexpressions = new ArrayList<>();
    }

    public plsql_statement_SelectStatement(
        boolean unique,        boolean bulk,        String selectList,        boolean isCount,        String from_,        boolean collect,        boolean distinct,        boolean all        ArrayList<Expression> expressions,        ArrayList<VarRefExpression> varrefexpressions    ) {
        this.unique = unique;
        this.bulk = bulk;
        this.selectList = selectList;
        this.isCount = isCount;
        this.from_ = from_;
        this.collect = collect;
        this.distinct = distinct;
        this.all = all;
        this.expressions = expressions;
        this.varrefexpressions = varrefexpressions;
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
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
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