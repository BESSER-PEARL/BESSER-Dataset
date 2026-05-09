





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniQuantifiedExpression extends ArmaniDesignRuleExpression {

    private String quantifier;





    private aspectualacme_ArmaniSetExpression aspectualacme_armanisetexpression;




    private aspectualacme_ArmaniDesignRuleExpression aspectualacme_armanidesignruleexpression;




    private aspectualacme_ArmaniVariable aspectualacme_armanivariable;


    public aspectualacme_ArmaniQuantifiedExpression(
        String quantifier    ) {
        super(
        );
        this.quantifier = quantifier;
    }


    public String getQuantifier() {
        return quantifier;
    }

    public void setQuantifier(String quantifier) {
        this.quantifier = quantifier;
    }

    public aspectualacme_ArmaniSetExpression getAspectualacme_armanisetexpression() {
        return aspectualacme_armanisetexpression;
    }

    public void setAspectualacme_armanisetexpression(aspectualacme_ArmaniSetExpression aspectualacme_armanisetexpression) {
        this.aspectualacme_armanisetexpression = aspectualacme_armanisetexpression;
    }
    public aspectualacme_ArmaniDesignRuleExpression getAspectualacme_armanidesignruleexpression() {
        return aspectualacme_armanidesignruleexpression;
    }

    public void setAspectualacme_armanidesignruleexpression(aspectualacme_ArmaniDesignRuleExpression aspectualacme_armanidesignruleexpression) {
        this.aspectualacme_armanidesignruleexpression = aspectualacme_armanidesignruleexpression;
    }
    public aspectualacme_ArmaniVariable getAspectualacme_armanivariable() {
        return aspectualacme_armanivariable;
    }

    public void setAspectualacme_armanivariable(aspectualacme_ArmaniVariable aspectualacme_armanivariable) {
        this.aspectualacme_armanivariable = aspectualacme_armanivariable;
    }

}