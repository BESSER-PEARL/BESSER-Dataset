





import java.util.List;
import java.util.ArrayList;

public class mpl_VariableReference extends AtomicExpression {






    private mpl_Variable mpl_variable;




    private mpl_Assignment mpl_assignment;


    public mpl_VariableReference(
    ) {
        super(
        );
    }



    public mpl_Variable getMpl_variable() {
        return mpl_variable;
    }

    public void setMpl_variable(mpl_Variable mpl_variable) {
        this.mpl_variable = mpl_variable;
    }
    public mpl_Assignment getMpl_assignment() {
        return mpl_assignment;
    }

    public void setMpl_assignment(mpl_Assignment mpl_assignment) {
        this.mpl_assignment = mpl_assignment;
    }

}