





import java.util.List;
import java.util.ArrayList;

public class mpl_Assignment extends Statement {






    private mpl_Expression mpl_expression;




    private mpl_VariableRefrence mpl_variablerefrence;


    public mpl_Assignment(
    ) {
        super(
        );
    }



    public mpl_Expression getMpl_expression() {
        return mpl_expression;
    }

    public void setMpl_expression(mpl_Expression mpl_expression) {
        this.mpl_expression = mpl_expression;
    }
    public mpl_VariableRefrence getMpl_variablerefrence() {
        return mpl_variablerefrence;
    }

    public void setMpl_variablerefrence(mpl_VariableRefrence mpl_variablerefrence) {
        this.mpl_variablerefrence = mpl_variablerefrence;
    }

}