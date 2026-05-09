





import java.util.List;
import java.util.ArrayList;

public class expressions_AdditiveExpression extends ShiftExpressionChild {






    private List<AdditiveExpressionChild> additiveexpressionchilds;




    private List<AdditiveOperator> additiveoperators;


    public expressions_AdditiveExpression(
    ) {
        super(
        );
        this.additiveexpressionchilds = new ArrayList<>();
        this.additiveoperators = new ArrayList<>();
    }

    public expressions_AdditiveExpression(
        ArrayList<AdditiveExpressionChild> additiveexpressionchilds,        ArrayList<AdditiveOperator> additiveoperators    ) {
        this.additiveexpressionchilds = additiveexpressionchilds;
        this.additiveoperators = additiveoperators;
    }


    public List<AdditiveExpressionChild> getAdditiveexpressionchilds() {
        return additiveexpressionchilds;
    }

    public void addAdditiveexpressionchild(Additiveexpressionchild additiveexpressionchild) {
        this.additiveexpressionchilds.add(additiveexpressionchild);
    }
    public List<AdditiveOperator> getAdditiveoperators() {
        return additiveoperators;
    }

    public void addAdditiveoperator(Additiveoperator additiveoperator) {
        this.additiveoperators.add(additiveoperator);
    }

}