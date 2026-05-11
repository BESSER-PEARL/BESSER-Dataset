





import java.util.List;
import java.util.ArrayList;

public class pascal_term  {

    private String multiplicativeoperator;





    private pascal_signedFactor pascal_signedfactor;




    private pascal_term pascal_term;




    private pascal_simpleExpression pascal_simpleexpression;


    public pascal_term(
        String multiplicativeoperator    ) {
        this.multiplicativeoperator = multiplicativeoperator;
    }


    public String getMultiplicativeoperator() {
        return multiplicativeoperator;
    }

    public void setMultiplicativeoperator(String multiplicativeoperator) {
        this.multiplicativeoperator = multiplicativeoperator;
    }

    public pascal_signedFactor getPascal_signedfactor() {
        return pascal_signedfactor;
    }

    public void setPascal_signedfactor(pascal_signedFactor pascal_signedfactor) {
        this.pascal_signedfactor = pascal_signedfactor;
    }
    public pascal_term getPascal_term() {
        return pascal_term;
    }

    public void setPascal_term(pascal_term pascal_term) {
        this.pascal_term = pascal_term;
    }
    public pascal_simpleExpression getPascal_simpleexpression() {
        return pascal_simpleexpression;
    }

    public void setPascal_simpleexpression(pascal_simpleExpression pascal_simpleexpression) {
        this.pascal_simpleexpression = pascal_simpleexpression;
    }

}