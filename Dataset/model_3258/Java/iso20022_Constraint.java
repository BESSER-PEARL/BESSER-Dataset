





import java.util.List;
import java.util.ArrayList;

public class iso20022_Constraint extends RepositoryConcept {

    private String expressionLanguage;
    private String expression;





    private iso20022_RepositoryConcept iso20022_repositoryconcept;




    private iso20022_RepositoryConcept iso20022_repositoryconcept;


    public iso20022_Constraint(
        String expressionLanguage,        String expression    ) {
        super(
        );
        this.expressionLanguage = expressionLanguage;
        this.expression = expression;
    }


    public String getExpressionlanguage() {
        return expressionLanguage;
    }

    public void setExpressionlanguage(String expressionLanguage) {
        this.expressionLanguage = expressionLanguage;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public iso20022_RepositoryConcept getIso20022_repositoryconcept() {
        return iso20022_repositoryconcept;
    }

    public void setIso20022_repositoryconcept(iso20022_RepositoryConcept iso20022_repositoryconcept) {
        this.iso20022_repositoryconcept = iso20022_repositoryconcept;
    }
    public iso20022_RepositoryConcept getIso20022_repositoryconcept() {
        return iso20022_repositoryconcept;
    }

    public void setIso20022_repositoryconcept(iso20022_RepositoryConcept iso20022_repositoryconcept) {
        this.iso20022_repositoryconcept = iso20022_repositoryconcept;
    }

}