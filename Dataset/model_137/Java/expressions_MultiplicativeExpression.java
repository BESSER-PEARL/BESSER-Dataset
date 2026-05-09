





import java.util.List;
import java.util.ArrayList;

public class expressions_MultiplicativeExpression extends AdditiveExpressionChild {






    private List<MultiplicativeExpressionChild> multiplicativeexpressionchilds;




    private List<MultiplicativeOperator> multiplicativeoperators;


    public expressions_MultiplicativeExpression(
    ) {
        super(
        );
        this.multiplicativeexpressionchilds = new ArrayList<>();
        this.multiplicativeoperators = new ArrayList<>();
    }

    public expressions_MultiplicativeExpression(
        ArrayList<MultiplicativeExpressionChild> multiplicativeexpressionchilds,        ArrayList<MultiplicativeOperator> multiplicativeoperators    ) {
        this.multiplicativeexpressionchilds = multiplicativeexpressionchilds;
        this.multiplicativeoperators = multiplicativeoperators;
    }


    public List<MultiplicativeExpressionChild> getMultiplicativeexpressionchilds() {
        return multiplicativeexpressionchilds;
    }

    public void addMultiplicativeexpressionchild(Multiplicativeexpressionchild multiplicativeexpressionchild) {
        this.multiplicativeexpressionchilds.add(multiplicativeexpressionchild);
    }
    public List<MultiplicativeOperator> getMultiplicativeoperators() {
        return multiplicativeoperators;
    }

    public void addMultiplicativeoperator(Multiplicativeoperator multiplicativeoperator) {
        this.multiplicativeoperators.add(multiplicativeoperator);
    }

}