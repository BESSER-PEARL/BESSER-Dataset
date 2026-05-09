





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniAdditiveExpression extends ArmaniExpression {

    private String operators;





    private aspectualacme_ArmaniRelationalExpression aspectualacme_armanirelationalexpression;




    private List<aspectualacme_ArmaniMultiplicativeExpression> aspectualacme_armanimultiplicativeexpressions;


    public aspectualacme_ArmaniAdditiveExpression(
        String operators    ) {
        super(
        );
        this.operators = operators;
        this.aspectualacme_armanimultiplicativeexpressions = new ArrayList<>();
    }

    public aspectualacme_ArmaniAdditiveExpression(
        String operators        ArrayList<aspectualacme_ArmaniMultiplicativeExpression> aspectualacme_armanimultiplicativeexpressions    ) {
        this.operators = operators;
        this.aspectualacme_armanimultiplicativeexpressions = aspectualacme_armanimultiplicativeexpressions;
    }

    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public aspectualacme_ArmaniRelationalExpression getAspectualacme_armanirelationalexpression() {
        return aspectualacme_armanirelationalexpression;
    }

    public void setAspectualacme_armanirelationalexpression(aspectualacme_ArmaniRelationalExpression aspectualacme_armanirelationalexpression) {
        this.aspectualacme_armanirelationalexpression = aspectualacme_armanirelationalexpression;
    }
    public List<aspectualacme_ArmaniMultiplicativeExpression> getAspectualacme_armanimultiplicativeexpressions() {
        return aspectualacme_armanimultiplicativeexpressions;
    }

    public void addAspectualacme_armanimultiplicativeexpression(Aspectualacme_armanimultiplicativeexpression aspectualacme_armanimultiplicativeexpression) {
        this.aspectualacme_armanimultiplicativeexpressions.add(aspectualacme_armanimultiplicativeexpression);
    }

}