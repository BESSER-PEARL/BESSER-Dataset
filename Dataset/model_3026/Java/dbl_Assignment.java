





import java.util.List;
import java.util.ArrayList;

public class dbl_Assignment extends SimpleStatement {






    private dbl_ForStatement dbl_forstatement;




    private dbl_Expression dbl_expression;


    public dbl_Assignment(
    ) {
        super(
        );
    }



    public dbl_ForStatement getDbl_forstatement() {
        return dbl_forstatement;
    }

    public void setDbl_forstatement(dbl_ForStatement dbl_forstatement) {
        this.dbl_forstatement = dbl_forstatement;
    }
    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }

}