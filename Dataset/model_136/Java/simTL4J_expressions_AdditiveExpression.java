





import java.util.List;
import java.util.ArrayList;

public class simTL4J_expressions_AdditiveExpression extends ShiftExpressionChild {






    private List<AdditiveOperator> additiveoperators;




    private List<AdditiveExpressionChild> additiveexpressionchilds;


    public simTL4J_expressions_AdditiveExpression(
    ) {
        super(
        );
        this.additiveoperators = new ArrayList<>();
        this.additiveexpressionchilds = new ArrayList<>();
    }

    public simTL4J_expressions_AdditiveExpression(
        ArrayList<AdditiveOperator> additiveoperators,        ArrayList<AdditiveExpressionChild> additiveexpressionchilds    ) {
        this.additiveoperators = additiveoperators;
        this.additiveexpressionchilds = additiveexpressionchilds;
    }


    public List<AdditiveOperator> getAdditiveoperators() {
        return additiveoperators;
    }

    public void addAdditiveoperator(Additiveoperator additiveoperator) {
        this.additiveoperators.add(additiveoperator);
    }
    public List<AdditiveExpressionChild> getAdditiveexpressionchilds() {
        return additiveexpressionchilds;
    }

    public void addAdditiveexpressionchild(Additiveexpressionchild additiveexpressionchild) {
        this.additiveexpressionchilds.add(additiveexpressionchild);
    }

}