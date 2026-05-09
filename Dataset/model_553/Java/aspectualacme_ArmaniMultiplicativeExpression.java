





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniMultiplicativeExpression extends ArmaniExpression {

    private String operators;





    private List<aspectualacme_ArmaniUnaryExpression> aspectualacme_armaniunaryexpressions;


    public aspectualacme_ArmaniMultiplicativeExpression(
        String operators    ) {
        super(
        );
        this.operators = operators;
        this.aspectualacme_armaniunaryexpressions = new ArrayList<>();
    }

    public aspectualacme_ArmaniMultiplicativeExpression(
        String operators        ArrayList<aspectualacme_ArmaniUnaryExpression> aspectualacme_armaniunaryexpressions    ) {
        this.operators = operators;
        this.aspectualacme_armaniunaryexpressions = aspectualacme_armaniunaryexpressions;
    }

    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public List<aspectualacme_ArmaniUnaryExpression> getAspectualacme_armaniunaryexpressions() {
        return aspectualacme_armaniunaryexpressions;
    }

    public void addAspectualacme_armaniunaryexpression(Aspectualacme_armaniunaryexpression aspectualacme_armaniunaryexpression) {
        this.aspectualacme_armaniunaryexpressions.add(aspectualacme_armaniunaryexpression);
    }

}