





import java.util.List;
import java.util.ArrayList;

public class c_sharp_expressions_ArrayCreationExpression extends PrimaryExpression {






    private Type type;




    private List<RankSpecifier> rankspecifiers;




    private ExpressionList expressionlist;




    private ArrayType arraytype;


    public c_sharp_expressions_ArrayCreationExpression(
    ) {
        super(
        );
        this.rankspecifiers = new ArrayList<>();
    }

    public c_sharp_expressions_ArrayCreationExpression(
        ArrayList<RankSpecifier> rankspecifiers    ) {
        this.rankspecifiers = rankspecifiers;
    }


    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public List<RankSpecifier> getRankspecifiers() {
        return rankspecifiers;
    }

    public void addRankspecifier(Rankspecifier rankspecifier) {
        this.rankspecifiers.add(rankspecifier);
    }
    public ExpressionList getExpressionlist() {
        return expressionlist;
    }

    public void setExpressionlist(ExpressionList expressionlist) {
        this.expressionlist = expressionlist;
    }
    public ArrayType getArraytype() {
        return arraytype;
    }

    public void setArraytype(ArrayType arraytype) {
        this.arraytype = arraytype;
    }

}