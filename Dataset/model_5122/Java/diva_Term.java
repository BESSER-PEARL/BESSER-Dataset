





import java.util.List;
import java.util.ArrayList;

public class diva_Term extends DiVAModelElement {






    private diva_Expression diva_expression;




    private diva_NaryTerm diva_naryterm;


    public diva_Term(
    ) {
        super(
        );
    }



    public diva_Expression getDiva_expression() {
        return diva_expression;
    }

    public void setDiva_expression(diva_Expression diva_expression) {
        this.diva_expression = diva_expression;
    }
    public diva_NaryTerm getDiva_naryterm() {
        return diva_naryterm;
    }

    public void setDiva_naryterm(diva_NaryTerm diva_naryterm) {
        this.diva_naryterm = diva_naryterm;
    }

}