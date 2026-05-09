





import java.util.List;
import java.util.ArrayList;

public class expressions_EqualityExpression extends AndExpressionChild {






    private List<EqualityExpressionChild> equalityexpressionchilds;


    public expressions_EqualityExpression(
    ) {
        super(
        );
        this.equalityexpressionchilds = new ArrayList<>();
    }

    public expressions_EqualityExpression(
        ArrayList<EqualityExpressionChild> equalityexpressionchilds    ) {
        this.equalityexpressionchilds = equalityexpressionchilds;
    }


    public List<EqualityExpressionChild> getEqualityexpressionchilds() {
        return equalityexpressionchilds;
    }

    public void addEqualityexpressionchild(Equalityexpressionchild equalityexpressionchild) {
        this.equalityexpressionchilds.add(equalityexpressionchild);
    }

}