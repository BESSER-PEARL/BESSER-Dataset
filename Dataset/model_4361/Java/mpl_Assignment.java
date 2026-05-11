





import java.util.List;
import java.util.ArrayList;

public class mpl_Assignment extends Form {






    private mpl_Expression mpl_expression;




    private mpl_VariableReference mpl_variablereference;


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
    public mpl_VariableReference getMpl_variablereference() {
        return mpl_variablereference;
    }

    public void setMpl_variablereference(mpl_VariableReference mpl_variablereference) {
        this.mpl_variablereference = mpl_variablereference;
    }

}