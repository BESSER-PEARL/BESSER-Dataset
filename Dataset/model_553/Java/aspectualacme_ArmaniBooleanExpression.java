





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniBooleanExpression extends ArmaniDesignRuleExpression {






    private List<aspectualacme_ArmaniOrExpression> aspectualacme_armaniorexpressions;


    public aspectualacme_ArmaniBooleanExpression(
    ) {
        super(
        );
        this.aspectualacme_armaniorexpressions = new ArrayList<>();
    }

    public aspectualacme_ArmaniBooleanExpression(
        ArrayList<aspectualacme_ArmaniOrExpression> aspectualacme_armaniorexpressions    ) {
        this.aspectualacme_armaniorexpressions = aspectualacme_armaniorexpressions;
    }


    public List<aspectualacme_ArmaniOrExpression> getAspectualacme_armaniorexpressions() {
        return aspectualacme_armaniorexpressions;
    }

    public void addAspectualacme_armaniorexpression(Aspectualacme_armaniorexpression aspectualacme_armaniorexpression) {
        this.aspectualacme_armaniorexpressions.add(aspectualacme_armaniorexpression);
    }

}