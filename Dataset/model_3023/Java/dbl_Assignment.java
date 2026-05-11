





import java.util.List;
import java.util.ArrayList;

public class dbl_Assignment extends SimpleStatement {






    private dbl_VariableAccess dbl_variableaccess;




    private dbl_Expression dbl_expression;


    public dbl_Assignment(
    ) {
        super(
        );
    }



    public dbl_VariableAccess getDbl_variableaccess() {
        return dbl_variableaccess;
    }

    public void setDbl_variableaccess(dbl_VariableAccess dbl_variableaccess) {
        this.dbl_variableaccess = dbl_variableaccess;
    }
    public dbl_Expression getDbl_expression() {
        return dbl_expression;
    }

    public void setDbl_expression(dbl_Expression dbl_expression) {
        this.dbl_expression = dbl_expression;
    }

}