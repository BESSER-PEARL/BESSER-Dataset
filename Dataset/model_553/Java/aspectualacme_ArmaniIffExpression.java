





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniIffExpression extends ArmaniExpression {






    private List<aspectualacme_ArmaniEqualityExpression> aspectualacme_armaniequalityexpressions;




    private aspectualacme_ArmaniImpliesExpression aspectualacme_armaniimpliesexpression;


    public aspectualacme_ArmaniIffExpression(
    ) {
        super(
        );
        this.aspectualacme_armaniequalityexpressions = new ArrayList<>();
    }

    public aspectualacme_ArmaniIffExpression(
        ArrayList<aspectualacme_ArmaniEqualityExpression> aspectualacme_armaniequalityexpressions    ) {
        this.aspectualacme_armaniequalityexpressions = aspectualacme_armaniequalityexpressions;
    }


    public List<aspectualacme_ArmaniEqualityExpression> getAspectualacme_armaniequalityexpressions() {
        return aspectualacme_armaniequalityexpressions;
    }

    public void addAspectualacme_armaniequalityexpression(Aspectualacme_armaniequalityexpression aspectualacme_armaniequalityexpression) {
        this.aspectualacme_armaniequalityexpressions.add(aspectualacme_armaniequalityexpression);
    }
    public aspectualacme_ArmaniImpliesExpression getAspectualacme_armaniimpliesexpression() {
        return aspectualacme_armaniimpliesexpression;
    }

    public void setAspectualacme_armaniimpliesexpression(aspectualacme_ArmaniImpliesExpression aspectualacme_armaniimpliesexpression) {
        this.aspectualacme_armaniimpliesexpression = aspectualacme_armaniimpliesexpression;
    }

}