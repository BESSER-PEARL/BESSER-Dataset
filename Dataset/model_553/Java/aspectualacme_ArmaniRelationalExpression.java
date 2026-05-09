





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniRelationalExpression extends ArmaniExpression {

    private String operators;





    private aspectualacme_ArmaniEqualityExpression aspectualacme_armaniequalityexpression;


    public aspectualacme_ArmaniRelationalExpression(
        String operators    ) {
        super(
        );
        this.operators = operators;
    }


    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public aspectualacme_ArmaniEqualityExpression getAspectualacme_armaniequalityexpression() {
        return aspectualacme_armaniequalityexpression;
    }

    public void setAspectualacme_armaniequalityexpression(aspectualacme_ArmaniEqualityExpression aspectualacme_armaniequalityexpression) {
        this.aspectualacme_armaniequalityexpression = aspectualacme_armaniequalityexpression;
    }

}